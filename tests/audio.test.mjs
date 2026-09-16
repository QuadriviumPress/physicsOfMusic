import assert from 'node:assert/strict';
import test from 'node:test';

// Bindery sets BASE_URL for deploy/CI. The default cases below assert root-
// relative URLs, so load the plugin once with that env cleared. The dedicated
// base-path test re-imports with BASE_URL set.
const savedBaseUrl = process.env.BASE_URL;
delete process.env.BASE_URL;
const { default: plugin, humanize, playerUrl, resolveClip, splitList } = await import(
  `../plugins/audio.mjs?root=${Date.now()}`
);
if (savedBaseUrl === undefined) delete process.env.BASE_URL;
else process.env.BASE_URL = savedBaseUrl;

const directive = plugin.directives.find(item => item.name === 'audio');
const run = (arg, options = {}, body = []) => directive.run({ arg, options, body }, null);
const isError = nodes =>
  nodes[0].type === 'paragraph' && nodes[0].children[0].children[0].value.startsWith('Audio error');

test('a bare id resolves to the generated clip and its companion figure', () => {
  const [figure] = run('ch05-sine');
  assert.equal(figure.kind, 'figure');
  const image = figure.children.find(child => child.type === 'image');
  assert.equal(image.url, '/images/ch05-sine.svg');
  const player = figure.children.find(child => child.type === 'iframe');
  assert.equal(player.src, '/audio-player.html#src=%2Faudio%2Fch05-sine.mp3&name=Sine');
  assert.equal(player.title, 'Sine — audio player');
  const link = JSON.stringify(figure.children.at(-1));
  assert.match(link, /\/audio\/ch05-sine\.mp3/);
});

test('each clip in a comparison gets an independent player', () => {
  const [figure] = run('a, b', { 'no-figure': true, names: 'First, Second' });
  const players = figure.children.filter(child => child.type === 'iframe');
  assert.equal(players.length, 2);
  assert.equal(players[1].src, playerUrl({ url: '/audio/b.mp3', name: 'Second' }));
});

test('paths and URLs are passed through untouched', () => {
  assert.deepEqual(resolveClip('https://example.org/a.wav'),
    { url: 'https://example.org/a.wav', id: 'a', isBare: false });
  assert.deepEqual(resolveClip('../audio/x.ogg'),
    { url: '../audio/x.ogg', id: 'x', isBare: false });
  assert.equal(resolveClip('ch05-sine').url, '/audio/ch05-sine.mp3');
  assert.equal(resolveClip('ch05-sine.wav').url, '/audio/ch05-sine.wav');
});

test('several clips need an explicit shared figure', () => {
  assert.ok(isError(run('a, b')), 'no :figure: is an error');
  const [figure] = run('a, b', { figure: '../images/pair.svg' });
  assert.equal(figure.children.find(child => child.type === 'image').url, '../images/pair.svg');
});

test(':no-figure: leaves the caption and links alone', () => {
  const [figure] = run('a, b', { 'no-figure': true });
  assert.equal(figure.children.some(child => child.type === 'image'), false);
  assert.equal(figure.children.at(-1).type, 'caption');
});

test(':names: must match the number of clips', () => {
  assert.ok(isError(run('a, b', { names: 'Only one' })));
  const [figure] = run('a, b', { figure: 'f.svg', names: 'First, Second' });
  const caption = JSON.stringify(figure.children.at(-1));
  assert.match(caption, /First/);
  assert.match(caption, /Second/);
});

test('the transcript is emitted, because it is all a print reader has', () => {
  const [figure] = run('ch05-sine', { transcript: 'A plain hollow tone.' });
  const caption = figure.children.at(-1);
  const transcript = caption.children.find(child => child.class === 'audio-transcript');
  assert.ok(transcript, 'transcript paragraph present');
  assert.match(JSON.stringify(transcript), /A plain hollow tone\./);
});

test(':no-link: suppresses the listen line', () => {
  const [figure] = run('ch05-sine', { 'no-link': true, transcript: 'x' });
  assert.equal(JSON.stringify(figure.children.at(-1)).includes('audio-link'), false);
});

test('a label makes the figure cross-referenceable', () => {
  const [figure] = run('ch05-sine', { label: 'Fig:Ch05-Sine' });
  assert.equal(figure.label, 'Fig:Ch05-Sine');
  assert.equal(figure.identifier, 'fig:ch05-sine');
});

test('the figure is one container, not a pair of lettered subfigures', () => {
  const [figure] = run('ch05-sine');
  assert.equal(figure.noSubcontainers, true);
});

test('a missing argument is reported rather than silently rendering nothing', () => {
  assert.ok(isError(run('')));
  assert.ok(isError(run(' , ')));
});

test('ids are made readable, with the chapter prefix dropped', () => {
  assert.equal(humanize('ch05-sawtooth-vs-square'), 'Sawtooth vs Square');
  assert.equal(humanize('ch12-timpani'), 'Timpani');
  assert.equal(humanize('just-major-third'), 'Just Major Third');
});

test('comma lists tolerate stray whitespace and empty entries', () => {
  assert.deepEqual(splitList(' a ,, b , '), ['a', 'b']);
  assert.deepEqual(splitList(undefined), []);
});

test('generated URLs honor the deployment base path', async () => {
  const originalBaseUrl = process.env.BASE_URL;
  process.env.BASE_URL = '/physicsOfMusic';
  try {
    const basedPlugin = await import(`../plugins/audio.mjs?base-path-test=${ Date.now() }`);
    const clip = basedPlugin.resolveClip('ch05-sine');
    assert.equal(clip.url, '/physicsOfMusic/audio/ch05-sine.mp3');
    assert.equal(
      basedPlugin.playerUrl({ ...clip, name: 'Sine' }),
      '/physicsOfMusic/audio-player.html#src=%2FphysicsOfMusic%2Faudio%2Fch05-sine.mp3&name=Sine'
    );
  }
  finally {
    if (originalBaseUrl === undefined) delete process.env.BASE_URL;
    else process.env.BASE_URL = originalBaseUrl;
  }
});
