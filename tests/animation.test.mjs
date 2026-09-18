import assert from 'node:assert/strict';
import test from 'node:test';

// Bindery sets BASE_URL for deploy/CI. The cases below assert root-relative
// URLs, so load the plugin once with that env cleared; the dedicated base-path
// test re-imports with BASE_URL set.
const savedBaseUrl = process.env.BASE_URL;
delete process.env.BASE_URL;
const { default: plugin } = await import( `../plugins/animation.mjs?root=${ Date.now() }` );
if ( savedBaseUrl === undefined ) {
  delete process.env.BASE_URL;
}
else {
  process.env.BASE_URL = savedBaseUrl;
}

const directive = plugin.directives.find( item => item.name === 'animation' );

/**
 * Minimal stand-in for the vfile MyST hands a directive, recording the
 * warnings the plugin reports rather than printing them.
 *
 * @returns {{messages: Array<Object>, message: function(string): Object}}
 */
function stubVFile() {
  const messages = [];
  return {
    messages,
    message( text ) {
      const entry = { message: text };
      messages.push( entry );
      return entry;
    }
  };
}

test( 'animation directive emits a live frame and a static fallback', () => {
  const body = [ { type: 'paragraph', children: [ { type: 'text', value: 'Caption' } ] } ];
  const [ container ] = directive.run( { arg: 'ch03-standing-wave-formation', body, options: {} }, stubVFile() );

  assert.equal( container.type, 'container' );
  assert.equal( container.kind, 'figure' );
  assert.equal( container.class, 'animation' );
  // Without this the iframe and the image are lettered (a) and (b).
  assert.equal( container.noSubcontainers, true );

  assert.deepEqual( container.children[ 0 ], {
    type: 'iframe',
    src: '/animations/ch03-standing-wave-formation.html',
    width: '100%',
    align: 'center',
    title: 'Standing Wave Formation — animation',
    class: 'animation-frame animation-aspect-2x1'
  } );
  assert.deepEqual( container.children[ 1 ], {
    type: 'image',
    url: '/images/ch03-standing-wave-formation.svg',
    alt: 'Static rendering of the Standing Wave Formation animation',
    width: '100%',
    align: 'center',
    class: 'animation-placeholder'
  } );
  assert.deepEqual( container.children[ 2 ], { type: 'caption', children: body } );
} );

test( 'options reach the frame, the fallback, and the figure', () => {
  const [ container ] = directive.run( {
    arg: 'ch06-beating.html',
    body: [],
    options: {
      figure: '/images/ch06-beats.svg',
      alt: 'Two tones beating',
      title: 'Beats',
      width: '80%',
      aspect: '16:9',
      align: 'left',
      class: 'animation-wide',
      label: 'fig:ch06-beating',
      enumerated: false
    }
  }, stubVFile() );

  assert.equal( container.children[ 0 ].src, '/animations/ch06-beating.html' );
  assert.equal( container.children[ 0 ].title, 'Beats' );
  assert.equal( container.children[ 0 ].width, '80%' );
  assert.equal( container.children[ 0 ].align, 'left' );
  assert.equal( container.children[ 0 ].class, 'animation-frame animation-aspect-16x9 animation-wide' );
  assert.equal( container.children[ 1 ].url, '/images/ch06-beats.svg' );
  assert.equal( container.children[ 1 ].alt, 'Two tones beating' );
  assert.equal( container.label, 'fig:ch06-beating' );
  assert.equal( container.identifier, 'fig:ch06-beating' );
  assert.equal( container.enumerated, false );
  // An empty body leaves the figure without a caption node.
  assert.equal( container.children.length, 2 );
} );

test( 'paths and URLs pass through untouched and need an explicit fallback', () => {
  const [ hosted ] = directive.run( {
    arg: 'https://animations.example/traveling-wave.html',
    body: [],
    options: { figure: '/images/ch03-traveling-wave.svg' }
  }, stubVFile() );

  assert.equal( hosted.children[ 0 ].src, 'https://animations.example/traveling-wave.html' );
  assert.equal( hosted.children[ 1 ].url, '/images/ch03-traveling-wave.svg' );

  const vfile = stubVFile();
  const [ error ] = directive.run( { arg: '../animations/local.html', body: [], options: {} }, vfile );

  assert.equal( error.type, 'paragraph' );
  assert.match( error.children[ 0 ].children[ 0 ].value, /explicit `:figure:`/ );
  assert.equal( vfile.messages.length, 1 );
  assert.equal( vfile.messages[ 0 ].fatal, false );
  assert.equal( vfile.messages[ 0 ].source, 'plugins/animation.mjs' );
} );

test( 'no-figure drops the fallback, and a missing argument is an error', () => {
  const [ frameOnly ] = directive.run( {
    arg: '../animations/local.html',
    body: [],
    options: { 'no-figure': true }
  }, stubVFile() );

  assert.equal( frameOnly.children.length, 1 );
  assert.equal( frameOnly.children[ 0 ].type, 'iframe' );

  const vfile = stubVFile();
  const [ error ] = directive.run( { arg: '', body: [], options: {} }, vfile );

  assert.match( error.children[ 0 ].children[ 0 ].value, /animation id, path, or URL is required/ );
  assert.equal( vfile.messages.length, 1 );
} );

test( 'animation URLs honor the deployment base path', async () => {
  const originalBaseUrl = process.env.BASE_URL;
  process.env.BASE_URL = '/physicsOfMusic';

  try {
    const { default: basedPlugin } = await import( `../plugins/animation.mjs?base-path-test=${ Date.now() }` );
    const basedDirective = basedPlugin.directives.find( item => item.name === 'animation' );
    const [ container ] = basedDirective.run( { arg: 'ch03-standing-wave-formation', body: [], options: {} }, stubVFile() );

    assert.equal( container.children[ 0 ].src, '/physicsOfMusic/animations/ch03-standing-wave-formation.html' );
    // The fallback stays unprefixed on purpose: MyST resolves an `image` node's
    // URL against the base path itself, but leaves an `iframe` `src` alone.
    assert.equal( container.children[ 1 ].url, '/images/ch03-standing-wave-formation.svg' );
  }
  finally {
    if ( originalBaseUrl === undefined ) {
      delete process.env.BASE_URL;
    }
    else {
      process.env.BASE_URL = originalBaseUrl;
    }
  }
} );
