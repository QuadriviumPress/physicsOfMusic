import assert from 'node:assert/strict';
import test from 'node:test';
import plugin, { parseTime, resolveVideo } from '../plugins/video.mjs';

const directive = plugin.directives.find(item => item.name === 'video');
const run = (arg, options = {}, body = []) => directive.run({ arg, options, body }, null);
const isError = nodes =>
  nodes[0].type === 'paragraph' && nodes[0].children[0].children[0].value.startsWith('Video error');

test('YouTube watch URLs become privacy-conscious embeds with an automatic poster', () => {
  const source = 'https://www.youtube.com/watch?v=spUNpyF58BY&t=1m30s';
  const [figure] = run(source, { 'video-title': 'Fourier transform' });
  assert.equal(figure.kind, 'figure');
  assert.equal(figure.noSubcontainers, true);
  assert.equal(
    figure.children[0].src,
    'https://www.youtube-nocookie.com/embed/spUNpyF58BY?start=90'
  );
  assert.equal(figure.children[0].title, 'Fourier transform');
  assert.equal(figure.children[1].url, 'https://i.ytimg.com/vi/spUNpyF58BY/hqdefault.jpg');
  assert.equal(figure.children[1].class, 'video-placeholder');
  assert.match(figure.children[1].alt, /Fourier transform/);
  assert.equal(figure.children[2].children[0].children[1].url, source);
});

test('common YouTube URL forms resolve to the same id', () => {
  const urls = [
    'https://youtu.be/spUNpyF58BY',
    'https://www.youtube.com/shorts/spUNpyF58BY',
    'https://www.youtube.com/live/spUNpyF58BY',
    'https://www.youtube.com/embed/spUNpyF58BY',
    'https://www.youtube-nocookie.com/embed/spUNpyF58BY'
  ];
  for (const url of urls) assert.equal(resolveVideo(url).id, 'spUNpyF58BY');
  assert.equal(
    resolveVideo('https://youtu.be/spUNpyF58BY#t=45s').embedUrl,
    'https://www.youtube-nocookie.com/embed/spUNpyF58BY?start=45'
  );
});

test('Vimeo path-style privacy hashes are carried into the player URL', () => {
  assert.equal(
    resolveVideo('https://vimeo.com/123456789/a1b2c3d4').embedUrl,
    'https://player.vimeo.com/video/123456789?h=a1b2c3d4'
  );
});

test('Vimeo uses an explicit poster and preserves unlisted-video data', () => {
  const source = 'https://vimeo.com/123456789?h=secret#t=42s';
  const [figure] = run(source, {
    poster: '/images/video-poster.jpg',
    'video-title': 'Plate modes',
    alt: 'Sand on a vibrating plate'
  });
  assert.equal(
    figure.children[0].src,
    'https://player.vimeo.com/video/123456789?h=secret#t=42s'
  );
  assert.equal(figure.children[1].url, '/images/video-poster.jpg');
  assert.equal(figure.children[1].alt, 'Sand on a vibrating plate');
  assert.equal(figure.children[2].children[0].children[1].url, source);
});

test('Vimeo without a poster reports a useful error', () => {
  const nodes = run('https://vimeo.com/123456789');
  assert.ok(isError(nodes));
  assert.match(JSON.stringify(nodes), /require.*poster/i);
});

test('unsupported and malformed URLs report errors instead of rendering', () => {
  assert.ok(isError(run('not a URL')));
  assert.ok(isError(run('https://example.test/video')));
  assert.ok(isError(run('https://youtube.com/watch?v=too-short')));
  assert.ok(isError(run('ftp://vimeo.com/123456789', { poster: 'poster.jpg' })));
});

test('caption content, source link, labels, and presentation options survive', () => {
  const body = [ { type: 'paragraph', children: [ { type: 'text', value: 'A useful caption.' } ] } ];
  const [figure] = run('https://youtu.be/spUNpyF58BY', {
    poster: '/images/custom.jpg',
    'video-title': 'Fourier',
    'link-text': 'Open the lesson',
    title: 'Play the Fourier lesson',
    width: '80%',
    aspect: '4:3',
    align: 'left',
    class: 'featured',
    label: 'Fig:Fourier-Video',
    enumerated: false
  }, body);
  assert.equal(figure.label, 'Fig:Fourier-Video');
  assert.equal(figure.identifier, 'fig:fourier-video');
  assert.equal(figure.enumerated, false);
  assert.equal(figure.children[0].width, '80%');
  assert.equal(figure.children[0].align, 'left');
  assert.equal(figure.children[0].title, 'Play the Fourier lesson');
  assert.match(figure.children[0].class, /video-aspect-4x3/);
  assert.match(figure.children[0].class, /featured/);
  assert.equal(figure.children[1].url, '/images/custom.jpg');
  assert.equal(figure.children[2].children[0], body[0]);
  assert.match(JSON.stringify(figure.children[2]), /Open the lesson/);
});

test('timestamp parsing accepts seconds and h/m/s notation', () => {
  assert.equal(parseTime('75'), 75);
  assert.equal(parseTime('1m15s'), 75);
  assert.equal(parseTime('2h3m4s'), 7384);
  assert.equal(parseTime('later'), null);
});
