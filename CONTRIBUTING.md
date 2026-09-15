# Contributing

Corrections, accessibility improvements, new exercises, better figures, and
build fixes are welcome. Substantial changes to the book's scope or chapter
order should be discussed in an issue first.

## Development environment

Use Node 22 and npm 10. The versions are declared in `.nvmrc`, `.node-version`,
and `package.json`. With nvm:

```bash
nvm use
npm ci
```

Preview with `npm start`. Before submitting a change, run:

```bash
npm run check
```

This validates chapter ordering and metadata, tests the plugins and scripts,
builds the site under `--strict`, and checks links. The tests require Python 3
as well as Node.

## Editing chapters

Follow the heading, directive, and exercise conventions in `README.md`. The page
outline is derived from the numbered `##` headings automatically. Every figure
needs useful `:alt:` text, every audio example needs a `:transcript:`, and every
reusable target needs a unique label.

Two failure modes are silent and are worth knowing about:

- **A title containing a colon must be quoted.** MyST accepts malformed
  frontmatter without complaint and then ignores every key in it, so the page
  builds but its `label:` never registers.
- **A simulation slug that does not exist produces no error.** The provider
  screenshot 404s and a generic placeholder card appears. Check the slug against
  the provider.

`npm run check:project` catches the first. Nothing catches the second but you.

Keep source attribution current in `SOURCES.md`. Record the source and licence
when adding adapted prose, data, or figures — and read the licence-compatibility
note at the top of that file before adapting anything new.

## The mathematical level

The main argument uses algebra, trigonometry, and logarithms, and no calculus.
This is a constraint on the *narrative*, not on the content: a derivation that
needs calculus belongs in a `{dropdown}`, marked optional, and nothing after it
may depend on having read it. A pull request that quietly moves calculus into
the running text will be asked to move it back.

## Generated assets

Three generators write files that are committed, because the Pages build runs
`myst build --html` and has nothing else available:

```bash
python3 -m pip install -r requirements-figures.txt

npm run check:figures      # matplotlib figures
npm run audio:render       # audio examples and their companion figures
npm run notation:render    # VexFlow staff notation
npm run notation:check
npm run audio:check
```

After changing a generator, run it and commit both the source and its output.
The matplotlib version is pinned because its SVG output is not stable across
versions.

Audio needs `ffmpeg`. MP3s are compared on existence and size rather than byte
for byte, because an MP3 is not reproducible across encoder versions the way a
pinned matplotlib's SVG is; the companion SVGs are compared exactly.

## Print and Word exports

The complete export toolchain is documented in `README.md`. Changes to
`plugins/`, `templates/`, `scripts/build-exports.sh`, or `scripts/tex-to-docx.py`
should be checked with at least one chapter offprint locally.

Run `npm run test:exports` with the print toolchain installed to build a small
fixture as full and student PDFs and as Word. It checks exercise and solution
visibility in the PDF text and verifies native Word equations and embedded
images.

## Accessibility

This book carries more media than most, and each kind has an obligation:

- Every figure has `:alt:` text that says what the figure shows, not what it is
  called.
- Every audio example has a `:transcript:` describing what is heard. Most
  readers, most of the time, are not listening.
- Every simulation has a caption that makes sense without the simulation, and a
  link that survives into print.

## Release checklist

1. Run `npm ci` and `npm run check` with Node 22.
2. Run `npm run check:figures`, `npm run audio:check`, `npm run notation:check`.
3. Run `npm run build:exports` and inspect the complete and student PDFs. Check
   that the staff-notation figures show notes rather than dingbats.
4. Confirm the student PDF omits solutions and that the DOCX contains math and
   figures.
5. Update the version-facing notes, then push a `v*` tag.
6. Confirm the Exports and Pages workflows and test all download links.
