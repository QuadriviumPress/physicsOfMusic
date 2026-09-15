import assert from 'node:assert/strict';
import test from 'node:test';
import { audioDirectives, chapterLists, figuresWithoutAlt, frontmatter } from '../scripts/validate-project.mjs';

test('chapter lists accept quoted paths, reordered keys, and nested navigation', () => {
  const result = chapterLists(`project:
    exports:
      - articles: [{file: "chapters/ch-01-test.md", level: 0}]
        id: book
    toc:
      - title: Part one
        children:
          - file: 'chapters/ch-01-test.md' # chapter
`);
  assert.deepEqual(result, { toc: ['chapters/ch-01-test.md'], exports: ['chapters/ch-01-test.md'] });
});

test('figure alt checks support all fences and nested directives', () => {
  for (const fence of ['```', '````', '~~~', '::::']) {
    assert.deepEqual(figuresWithoutAlt(`${fence}{figure} image.png\n:alt: A plot\n${fence}`), []);
    assert.deepEqual(figuresWithoutAlt(`${fence}{figure} image.png\n${fence}`), ['image.png']);
  }
  assert.deepEqual(figuresWithoutAlt('::::{solution}\n:::{figure} nested.png\n:::\n::::'), ['nested.png']);
  assert.deepEqual(figuresWithoutAlt('````markdown\n```{figure} example.png\n```\n````'), []);
  assert.deepEqual(figuresWithoutAlt('````\n```{figure} example.png\n```\n````'), []);
});

test('frontmatter parsing catches the unquoted-colon title that MyST ignores silently', () => {
  const good = frontmatter('---\ntitle: "Percussion: Membranes"\nlabel: ch-percussion\n---\n\nBody.\n');
  assert.equal(good.ok, true);
  assert.equal(good.data.label, 'ch-percussion');

  const bad = frontmatter('---\ntitle: Percussion: Membranes\n---\n\nBody.\n');
  assert.equal(bad.ok, false);
  assert.match(bad.error, /mapping/i);

  assert.equal(frontmatter('No frontmatter at all.\n').ok, false);
});

test('audio directives are found with their clips and figures', () => {
  const source = [
    '```{audio} ch05-sine',
    ':transcript: A plain tone.',
    '',
    'Caption.',
    '```',
    '',
    ':::{audio} ch05-sine, ch05-square',
    ':figure: ../images/ch05-pair.svg',
    ':names: Sine, Square',
    '',
    'Caption.',
    ':::',
    '',
    '```{audio} ch09-just-third',
    ':no-figure:',
    '```',
  ].join('\n');

  const found = audioDirectives(source);
  assert.equal(found.length, 3);
  assert.deepEqual(found[0].clips, ['ch05-sine']);
  assert.equal(found[0].figure, null, 'a single clip defaults its figure');
  assert.equal(found[0].noFigure, false);
  assert.deepEqual(found[1].clips, ['ch05-sine', 'ch05-square']);
  assert.equal(found[1].figure, '../images/ch05-pair.svg');
  assert.equal(found[2].noFigure, true);
});
