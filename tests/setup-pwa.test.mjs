import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import test from 'node:test';
import { fileURLToPath } from 'node:url';

// `scripts/setup-pwa.mjs` is a top-level script keyed on `process.cwd()`, not an
// importable module, so each case runs it against a throwaway build tree. Like
// the plugins, it reads BASE_URL once at startup; unlike them, it bakes the
// result into the manifest, the service-worker scope, and every HTML page, so a
// wrong prefix breaks installation and offline reading rather than one embed.
const repoRoot = fileURLToPath( new URL( '..', import.meta.url ) );
const script = path.join( repoRoot, 'scripts', 'setup-pwa.mjs' );

const MINIMAL_CONFIG = `version: 1
project:
  title: Physics of Music
  short_title: Physics
  description: A book about sound.
`;

const PAGE = '<html><head><title>Ch 1</title></head><body><p>Text</p></body></html>\n';

/**
 * Builds a throwaway project tree and runs the PWA setup script in it.
 *
 * @param {Object} [options]
 * @param {string} [options.baseUrl] - BASE_URL for the run; unset when omitted.
 * @param {string} [options.config] - Contents of `myst.yml`.
 * @param {Object<string,string>} [options.pages] - Extra files to seed under `_build/html`.
 * @returns {{dir: string, run: function(string=): Object, read: function(string): string, manifest: function(): Object}}
 */
function project( { baseUrl, config = MINIMAL_CONFIG, pages = { 'index.html': PAGE } } = {} ) {
  const dir = fs.mkdtempSync( path.join( os.tmpdir(), 'setup-pwa-' ) );
  test.after( () => fs.rmSync( dir, { recursive: true, force: true } ) );

  fs.writeFileSync( path.join( dir, 'myst.yml' ), config );
  fs.mkdirSync( path.join( dir, 'images' ), { recursive: true } );
  fs.copyFileSync( path.join( repoRoot, 'images', 'logo.svg' ), path.join( dir, 'images', 'logo.svg' ) );
  fs.mkdirSync( path.join( dir, 'pwa' ), { recursive: true } );
  for ( const file of [ 'offline.html', 'service-worker.js' ] ) {
    fs.copyFileSync( path.join( repoRoot, 'pwa', file ), path.join( dir, 'pwa', file ) );
  }
  for ( const [ name, contents ] of Object.entries( pages ) ) {
    const target = path.join( dir, '_build', 'html', name );
    fs.mkdirSync( path.dirname( target ), { recursive: true } );
    fs.writeFileSync( target, contents );
  }

  const read = name => fs.readFileSync( path.join( dir, '_build', 'html', name ), 'utf8' );
  return {
    dir,
    read,
    manifest: () => JSON.parse( read( 'manifest.webmanifest' ) ),
    run() {
      const env = { ...process.env };
      if ( baseUrl === undefined ) {
        delete env.BASE_URL;
      }
      else {
        env.BASE_URL = baseUrl;
      }
      return spawnSync( process.execPath, [ script ], { cwd: dir, env, encoding: 'utf8' } );
    }
  };
}

test( 'served from the domain root, every generated URL stays root-relative', () => {
  const build = project();
  const result = build.run();
  assert.equal( result.status, 0, result.stderr );

  const manifest = build.manifest();
  assert.equal( manifest.start_url, '/' );
  assert.equal( manifest.scope, '/' );
  assert.equal( manifest.name, 'Physics of Music' );
  assert.equal( manifest.short_name, 'Physics' );
  assert.deepEqual( manifest.icons.map( icon => icon.src ), [
    '/icons/icon-192.png',
    '/icons/icon-192-maskable.png',
    '/icons/icon-512.png',
    '/icons/icon-512-maskable.png'
  ] );

  const html = build.read( 'index.html' );
  assert.match( html, /<link rel="manifest" href="\/manifest\.webmanifest">/ );
  assert.match( html, /<link rel="apple-touch-icon" href="\/icons\/icon-192\.png">/ );
  assert.match( html, /serviceWorker\.register\('\/service-worker\.js', \{ scope: '\/' \}\)/ );
} );

test( 'served from a project subpath, BASE_URL prefixes the manifest, icons, and worker scope', () => {
  // A page in a subdirectory: the injected URLs are root-relative, so they must
  // not pick up the page's own depth.
  const build = project( { baseUrl: '/physicsOfMusic', pages: { 'chapters/ch01.html': PAGE } } );
  const result = build.run();
  assert.equal( result.status, 0, result.stderr );

  const manifest = build.manifest();
  // A trailing slash is required: a scope of `/physicsOfMusic` would also match
  // a sibling `/physicsOfMusicNotes/`, and `start_url` would resolve one level up.
  assert.equal( manifest.start_url, '/physicsOfMusic/' );
  assert.equal( manifest.scope, '/physicsOfMusic/' );
  assert.equal( manifest.icons[ 0 ].src, '/physicsOfMusic/icons/icon-192.png' );

  const html = build.read( 'chapters/ch01.html' );
  assert.match( html, /<link rel="manifest" href="\/physicsOfMusic\/manifest\.webmanifest">/ );
  assert.match( html, /<link rel="apple-touch-icon" href="\/physicsOfMusic\/icons\/icon-192\.png">/ );
  assert.match(
    html,
    /serviceWorker\.register\('\/physicsOfMusic\/service-worker\.js', \{ scope: '\/physicsOfMusic\/' \}\)/
  );
  assert.match( result.stdout, /scope \/physicsOfMusic\// );
} );

test( 'stray slashes in BASE_URL collapse to one clean prefix', () => {
  const build = project( { baseUrl: '//physicsOfMusic//' } );
  assert.equal( build.run().status, 0 );

  assert.equal( build.manifest().scope, '/physicsOfMusic/' );
  assert.equal( build.manifest().icons[ 0 ].src, '/physicsOfMusic/icons/icon-192.png' );
} );

test( 'a second run neither duplicates the injected tags nor changes the URLs', () => {
  const build = project( { baseUrl: '/physicsOfMusic' } );
  assert.equal( build.run().status, 0 );
  const once = build.read( 'index.html' );
  assert.equal( build.run().status, 0 );

  assert.equal( build.read( 'index.html' ), once );
  assert.equal( once.match( /rel="manifest"/g ).length, 1 );
  assert.equal( once.match( /serviceWorker\.register/g ).length, 1 );
} );

test( 'the run also lazy-loads H5P embeds and drops the duplicate /build/h5p copy', () => {
  const build = project( {
    baseUrl: '/physicsOfMusic',
    pages: {
      'index.html':
        '<html><head></head><body>' +
        '<iframe src="/physicsOfMusic/h5p/embed.html?id=ch04-review"></iframe>' +
        '<iframe loading="eager" src="/physicsOfMusic/h5p/embed.html?id=ch05-review"></iframe>' +
        '<iframe src="/physicsOfMusic/animations/ch03.html"></iframe>' +
        '</body></html>\n',
      'build/h5p/embed.html': '<html></html>\n'
    }
  } );
  assert.equal( build.run().status, 0 );

  const html = build.read( 'index.html' );
  assert.match( html, /<iframe loading="lazy" src="[^"]*h5p\/embed\.html\?id=ch04-review"/ );
  // An explicit loading= is left alone, and non-H5P frames are untouched.
  assert.match( html, /<iframe loading="eager" src="[^"]*id=ch05-review"/ );
  assert.match( html, /<iframe src="[^"]*animations\/ch03\.html"/ );
  assert.equal( fs.existsSync( path.join( build.dir, '_build', 'html', 'build', 'h5p' ) ), false );
} );

test( 'a missing MyST build is a hard error rather than a half-configured site', () => {
  const build = project( { pages: {} } );
  fs.rmSync( path.join( build.dir, '_build' ), { recursive: true, force: true } );

  const result = build.run();
  assert.notEqual( result.status, 0 );
  assert.match( result.stderr, /Missing _build\/html/ );
} );
