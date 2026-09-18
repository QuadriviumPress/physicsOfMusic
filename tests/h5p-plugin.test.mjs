import assert from 'node:assert/strict';
import test from 'node:test';

import plugin from '../plugins/h5p.mjs';

const directive = plugin.directives.find( item => item.name === 'h5p' );

test( 'H5P directive emits a lazy activity and a static fallback', () => {
  const body = [ { type: 'paragraph', children: [ { type: 'text', value: 'Static equivalent' } ] } ];
  const [ wrapper ] = directive.run( { arg: 'ch04-new-activity', body, options: {} }, {} );

  assert.equal( wrapper.type, 'div' );
  assert.equal( wrapper.class, 'h5p' );
  assert.deepEqual( wrapper.children[ 0 ], {
    type: 'iframe',
    src: '/h5p/embed.html?id=ch04-new-activity',
    width: '100%',
    align: 'center',
    title: 'Interactive activity — New Activity',
    loading: 'lazy',
    class: 'h5p-frame'
  } );
  assert.equal( wrapper.children[ 1 ].class, 'h5p-fallback' );
  assert.deepEqual( wrapper.children[ 1 ].children, body );
} );

test( 'H5P directive accepts externally hosted activity paths', () => {
  const body = [ { type: 'paragraph', children: [] } ];
  const [ wrapper ] = directive.run( {
    arg: 'https://activities.example/activity.html',
    body,
    options: { title: 'Hosted activity', class: 'h5p-tall' }
  }, {} );

  assert.equal( wrapper.children[ 0 ].src, 'https://activities.example/activity.html' );
  assert.equal( wrapper.children[ 0 ].title, 'Hosted activity' );
  assert.equal( wrapper.children[ 0 ].class, 'h5p-frame h5p-tall' );
} );
