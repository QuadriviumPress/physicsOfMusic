# MyST plugins

Six plugins, and the first five are about the same problem: the website can do
things paper cannot, and the book has to survive being printed anyway.

- [`simulation.mjs`](simulation.mjs) — embeds a running browser simulation on
  the website and falls back to a screenshot, a caption, and a link everywhere
  else. Provides `{simulation}`, `{openlyceum}`, `{phet}`, `{phet-legacy}`.
- [`audio.mjs`](audio.mjs) — builds an audio-example figure: inline website
  controls, the waveform and spectrum of a clip, a transcript, and a durable
  link. Provides `{audio}` (alias `{sound}`).
- [`animation.mjs`](animation.mjs) — embeds one of the book's own short,
  looping animations on the website and falls back to the matching static SVG
  figure everywhere else. Provides `{animation}` (alias `{anim}`).
- [`video.mjs`](video.mjs) — embeds a YouTube or Vimeo video on the website and
  falls back to a poster image and a durable source link everywhere else.
  Provides `{video}`.
- [`h5p.mjs`](h5p.mjs) — embeds one of the book's own self-hosted H5P
  "check your understanding" exercises and falls back to the question, written
  out ungraded, everywhere else. Provides `{h5p}`.
- [`export.mjs`](export.mjs) — rewrites the node types no export renderer
  handles into ones every renderer handles. Inert unless `MYST_PRINT` is set.

The five `.mjs` media plugins are registered in [`../myst.yml`](../myst.yml)
alongside `export.mjs`:

```yaml
project:
  plugins:
    - plugins/simulation.mjs
    - plugins/audio.mjs
    - plugins/animation.mjs
    - plugins/video.mjs
    - plugins/h5p.mjs
    - plugins/export.mjs
site:
  options:
    style: css/custom.css
```

The stylesheet the simulation, animation, video, and H5P plugins depend on lives in
[`../css/custom.css`](../css/custom.css), not beside the plugins: MyST's
`site.options.style` takes exactly one file, and the book needs all media rules
in that file. Sections 1, 3, 4, and 5 of that file are load-bearing — without
them every simulation, animation, video, or H5P exercise has its static
fallback sitting underneath it. That is graceful degradation rather than a
break, but it is why the stylesheet is registered.

Edits to a `.mjs` plugin do **not** hot-reload. Restart `myst start` after
changing one.

# The simulation plugin

Vendored unmodified from
[`modernPhysics`](https://github.com/QuadriviumPress/modernPhysics), where it is
byte-identical to the copies in `opticsTextbook` and `quantumMechanics`. Keep it
that way: fix bugs upstream and re-copy, rather than editing here.

## Usage

````markdown
```{openlyceum} StandingWaves
:label: fig:ch03-standing-waves-sim

Drive one end of the string and sweep the frequency; the string ignores you
until you hit a harmonic, and then it ignores everything else.
```
````

The figure is numbered and cross-referenced like any other:
`@fig:ch03-standing-waves-sim`.

Four directives, one implementation:

| Directive | Argument | Resolves to |
|---|---|---|
| `{openlyceum}` | repository name | `https://openlyceum.github.io/<Repo>/` |
| `{phet}` | simulation name | `https://phet.colorado.edu/sims/html/<sim>/latest/<sim>_<locale>.html` |
| `{phet-legacy}` | simulation name, or `project/sim` | `https://phet.colorado.edu/sims/cheerpj/<project>/latest/<project>.html?simulation=<sim>` |
| `{simulation}` (alias `{sim}`) | a URL, or `provider:name` | whatever you give it |

Anything that runs in an iframe works — the plugin is not tied to SceneryStack.
A bare URL just needs a `:placeholder:` to look right in a PDF.

## Options

| Option | Default | Notes |
|---|---|---|
| `width` | `100%` | **Percentages only.** The theme mangles `px` values. |
| `aspect` | `1024:618` (OpenLyceum), `768:504` (PhET), `4:3` (PhET legacy) | Other ratios need a matching rule in `../css/custom.css`. |
| `placeholder` | provider screenshot | Relative to the `.md` file, `/`-prefixed for the project root, or a URL. Use **PNG or JPEG**. |
| `no-placeholder` | — | Drop the static fallback entirely. |
| `alt` | derived | Alternative text for the fallback image. |
| `title` | derived | Accessible title for the iframe. |
| `align` | `center` | `left`, `center`, `right`. |
| `label` | — | Makes the figure cross-referenceable. |
| `class` | — | Extra classes on the simulation frame. |
| `enumerated` | — | Whether the figure is numbered. |
| `params` | — | Raw query string, e.g. `snapToGrid=true`. |
| `screens` / `screen` | — | `?screens=` / `?initialScreen=`. |
| `locale` | `en` | SceneryStack reads `?locale=`; PhET puts it in the filename. |
| `sim-name` | the id made readable | Display name — caption link, iframe title, alt text. |
| `link-text` | the simulation name | Text of the caption link. |
| `no-link` | — | Suppress the caption link. |

## How the fallback works

A simulation is a JavaScript application, so it can only ever *run* on the
website. MyST reflects that: the `iframe` node is rendered by the site theme and
by nothing else. MyST plugins cannot supply renderers for export formats, and
transforms run before any format-specific rendering, so nothing in the tree can
tell a plugin which format is being built. The fallback therefore has to be
structural. Each directive emits **both** an `iframe` node and a plain `image`
node as siblings inside one `figure` container, and each renderer keeps
whichever of the two it understands:

| Output | `iframe` | fallback `image` | Result |
|---|---|---|---|
| HTML site | live simulation | hidden by `custom.css` | the simulation |
| Browser print | hidden by `@media print` | shown by `@media print` | the screenshot |
| `--pdf` / `--tex` | dropped by `export.mjs` | `\includegraphics` | screenshot + caption |
| `--docx` | unsupported, skipped | embedded image | screenshot + caption |
| `--md` | folded away | becomes the `{figure}` argument | figure + link |

The caption always ends with a link to the live simulation. That link is the one
piece of the fallback that survives in every format.

Two deliberate non-choices, both of which look like obvious simplifications and
are not: the iframe gets no `placeholder` child (that is what stops Typst from
printing the screenshot twice), and the fallback image is not marked
`placeholder: true` (MyST's placeholder promotion runs only for tex/typst/docx,
only if the URL extension is valid for that format, and leaves `myst-to-md`'s
figure handler dereferencing an undefined `node.source`).

## Screenshots

`{openlyceum}` uses `Baton/screenshots/<Repo>.png` — captures of the running
simulation, refreshed by Baton's own workflow — not the generic
`screenshots/wide.png` PWA splash each simulation publishes. `{phet}` uses
`<sim>-600.png`, the largest size PhET publishes.

Both are remote URLs. MyST downloads and caches them into `_build/`, so exports
work offline after the first build, but the *first* build of a new simulation
needs network access. **A simulation slug that does not exist produces no error**
— the screenshot 404s and the generic placeholder card appears instead — so
verify a new slug against the provider before citing it.

## Adding a provider

`PROVIDERS` at the top of `simulation.mjs` is a plain object. An entry needs a
`resolve( id, options )` returning the simulation URL and a screenshot URL, plus
the frame's aspect ratio. If the aspect ratio is not already in
`../css/custom.css`, add a rule for it there.

# The audio plugin

A book about music has to be able to show its examples and let a reader hear
them. Nothing else in the Quadrivium fleet does this — the two music-theory
books link raw `.mp3` and `.wav` files with bare Markdown — so this plugin is
new.

## Usage

````markdown
```{audio} ch05-sawtooth
:label: fig:ch05-sawtooth
:transcript: A buzzy, nasal tone at 220 Hz, brighter than a sine at the same pitch.

Every harmonic of 220 Hz is present, with amplitude falling as 1/n.
```
````

A bare id resolves to `/audio/<id>.mp3`, and the figure defaults to
`/images/<id>.svg` — the two files each generator in
[`../scripts/audio/`](../scripts/audio/) writes as a pair, so the common case
needs neither option. A path or URL is passed through untouched.

The player itself is [`../audio-player.html`](../audio-player.html) in a MyST
`iframe` node. The project declares that page and [`../audio/`](../audio/) as
`static_files`, preserving their URLs instead of applying MyST's normal content
hashing. Raw `<audio>` HTML still does not survive MyST parsing; keep using the
directive.

Several clips in one figure — the usual case for a comparison — are named
comma-separated, and then the shared figure must be given explicitly:

````markdown
```{audio} ch05-sine, ch05-sawtooth, ch05-square
:names: Sine, Sawtooth, Square
:figure: ../images/ch05-three-waveforms.svg
:label: fig:ch05-three-waveforms
:transcript: Three tones at the same pitch and level; the sine is hollow, the
  sawtooth buzzy, the square reedy and missing every even harmonic.

The same fundamental, three spectra.
```
````

## Options

| Option | Default | Notes |
|---|---|---|
| `figure` | `/images/<id>.svg` | Required when the directive names several clips. |
| `no-figure` | — | Drop the figure; leaves caption and links only. |
| `names` | each id made readable | Comma-separated labels, one per clip. |
| `transcript` | — | One sentence on what the clip sounds like. **Strongly recommended** — see below. |
| `alt` | derived | Alternative text for the figure. |
| `width` | `100%` | Width of the figure. |
| `align` | `center` | `left`, `center`, `right`. |
| `label` | — | Makes the figure cross-referenceable. |
| `class` | — | Extra classes. |
| `enumerated` | — | Whether the figure is numbered. |
| `link-text` | the clip name | Text of the caption link. |
| `no-link` | — | Suppress the caption link. |

## Why there is no inline player

The obvious implementation is an `<audio controls>` element, and it does not
survive. This was established by probing the actual build, not assumed:

- **Raw `<audio>` is stripped.** MyST parses raw HTML at the document stage and
  converts what it can to mdast. `<div>` survives as a `div` node and
  `<iframe>` as an `iframe` node, but `<audio>` has no mdast equivalent and is
  removed outright, leaving nothing on the page. A plugin emitting an `html`
  node fares no better — it never reaches the renderer.
- **mystmd 1.10.1 has no `{audio}` or `{video}` directive** of its own.
  `{video}` parses as an unrecognized `mystDirective` and renders nothing.
- **An `iframe` player cannot find its clip.** MyST content-hashes and copies a
  locally linked media file and rewrites the URL — `/audio/ch05-sine.mp3`
  becomes `/build/ch05-sine-<hash>.mp3` — so the path the clip actually lands
  on is not knowable when the directive runs, and an `iframe` `src` is never
  processed that way. There is also no static-passthrough directory (`public/`
  and `_static/` are both ignored) to sidestep the hashing with.

So the figure is built from nodes MyST renders natively, and the reader listens
by following a link. That asset handling is the one thing to be glad of here: a
`link` to `/audio/<id>.mp3` is exactly what makes MyST copy the clip into the
site at all.

What the plugin adds over a bare link is the part that carries the physics: the
waveform-and-spectrum figure showing what is actually in the clip, a transcript,
and one numbered, cross-referenceable figure that is identical in every output
format.

| Output | figure | links |
|---|---|---|
| HTML site | shown | clickable, hashed URLs |
| PDF / DOCX / print | `\includegraphics` | printed as URLs |

**Write the transcript.** It is the only thing a reader has who is holding the
PDF, is deaf or hard of hearing, or is reading somewhere they cannot play sound
— which is most readers, most of the time.

## Where the clips come from

They are **synthesized, not sampled**: `../scripts/audio/chNN_audio.py` writes
each clip and its matching figure, so every example is reproducible, and the
book carries no third-party recording and no licence question. Generated `.mp3`
and `.svg` are committed, because the Pages build runs `myst build --html` with
no Python. Regenerate with `npm run audio:render`.

Two clips of the same musical idea must be equal in **level**, not in peak
amplitude, or the comparison is about loudness rather than timbre — a square
wave and a sine of equal peak differ by about 3 dB in RMS, and a listener will
report the square as louder and call it brighter. `audiolib.match_level`
normalizes to constant RMS; do not bypass it. RMS is a proxy for loudness rather
than loudness itself, and `audiolib` says where that approximation is thin.

# The animation plugin

A few figures show something that is inherently time-varying — a traveling
wave, a standing wave forming, two tones beating, a resonance curve sweeping
through a peak — and a static snapshot, or a strip of snapshots, is a weaker
explanation than watching it happen.

## Usage

````markdown
```{animation} ch03-standing-wave-formation
:label: fig:ch03-standing-wave-formation
:alt: Five stacked panels showing a right-going dashed wave, a left-going dashed wave, and their solid sum, at five successive moments. The sum changes amplitude but its zero crossings stay at the same positions, marked with red dots.

A right-going wave and a left-going wave of the same frequency and amplitude, added continuously. The sum does not travel. It stands still and breathes: the whole pattern grows, shrinks, inverts, and grows again, but the points where it crosses zero never move.
```
````

A bare id resolves to `/animations/<id>.html`, and the static fallback defaults
to `/images/<id>.svg` — by convention the same basename as the existing
matplotlib figure it replaces on the website, generated by
[`../scripts/figures/`](../scripts/figures/). The figure is numbered and
cross-referenced like any other: `@fig:ch03-standing-wave-formation`.

## Options

| Option | Default | Notes |
|---|---|---|
| `figure` | `/images/<id>.svg` | Required when the argument is a path or URL rather than a bare id. |
| `no-figure` | — | Drop the static fallback entirely. Only for an animation with no matching static figure. |
| `alt` | derived | Alternative text for the fallback image. Reuse the static figure's existing alt text where one already exists. |
| `title` | derived | Accessible title for the iframe. |
| `width` | `100%` | **Percentages only.** The theme mangles `px` values. |
| `aspect` | `2:1` | A single wide plot panel. Other ratios need a matching rule in `../css/custom.css`. |
| `align` | `center` | `left`, `center`, `right`. |
| `label` | — | Makes the figure cross-referenceable. |
| `class` | — | Extra classes on the animation frame. |
| `enumerated` | — | Whether the figure is numbered. |

## Writing an animation page

Each animation is a small, self-contained HTML page under
[`../animations/`](../animations/), named to match the id used in the
directive (`ch03-standing-wave-formation` → `animations/ch03-standing-wave-formation.html`).
It draws on a `<canvas>` using the shared runtime in
[`../animations/lib/animlib.js`](../animations/lib/animlib.js): device-pixel-ratio
canvas setup, a `requestAnimationFrame` loop with a play/pause toggle that
starts paused for readers who asked for reduced motion, a data-to-pixel
coordinate mapper, and curve-drawing helpers using the same palette as
`scripts/figures/figstyle.py` (`COLORS.blue`, `.red`, `.green`, …). The page
also links [`../animations/lib/animlib.css`](../animations/lib/animlib.css)
for the control-bar styling. Copy the skeleton of an existing page (e.g.
`ch03-standing-wave-formation.html`) rather than starting from a blank file.

There is no build step for these pages — open one directly in a browser while
iterating, then reference it from the chapter.

## How the fallback works

The mechanism is identical to `{simulation}`, with one simplification: there is
no external provider and no screenshot to fetch, because the fallback is
simply the static SVG the matching `scripts/figures/chNN_figures.py` function
already generates and commits. Each directive emits **both** an `iframe` node
and a plain `image` node as siblings inside one `figure` container, and each
renderer keeps whichever it understands:

| Output | `iframe` | fallback `image` | Result |
|---|---|---|---|
| HTML site | live animation | hidden by `custom.css` | the animation |
| Browser print | hidden by `@media print` | shown by `@media print` | the static figure |
| `--pdf` / `--tex` | dropped by `export.mjs` | `\includegraphics` | figure + caption |
| `--docx` | unsupported, skipped | embedded image | figure + caption |
| `--md` | folded away | becomes the `{figure}` argument | figure |

A bare id resolves to a root-relative `/animations/<id>.html` URL rather than a
path relative to the source `.md` file, for the same reason `{audio}`'s player
URL is root-relative: MyST does not resolve a relative path written into an
`iframe` node the way it resolves one in a `link` or `image` node, so a
relative id would break on any chapter page nested below the project root.
`project.static_files` in `myst.yml` declares `animations` to keep those URLs
stable and unhashed, the same way it declares `audio` and `audio-player.html`.

# The video plugin

`{video}` embeds a YouTube or Vimeo player on the website while keeping the
book useful in PDF, Word, Markdown, and browser print. Static outputs receive a
poster image and an ordinary link to the source video.

## Usage

YouTube supplies a stable thumbnail, so its common case needs no `:poster:`:

````markdown
```{video} https://www.youtube.com/watch?v=spUNpyF58BY
:video-title: But What Is the Fourier Transform? A Visual Introduction
:label: fig:fourier-video
:alt: Rotating arrows combine to trace a waveform.

Grant Sanderson builds the Fourier transform from rotating vectors.
```
````

Vimeo does not publish a thumbnail URL that can be derived from the numeric
video id. Give it a local or remote poster explicitly:

````markdown
```{video} https://vimeo.com/123456789
:video-title: Modes of a vibrating plate
:poster: /images/ch12-vibrating-plate-video.jpg
:alt: Sand gathers along the nodal lines of a vibrating metal plate.

A demonstration of successive Chladni patterns.
```
````

The argument must be a complete URL. Normal YouTube watch, short, live, and
embed URLs plus `youtu.be` links are accepted; normal Vimeo and Vimeo player
URLs are accepted. The iframe uses `youtube-nocookie.com` for YouTube. The link
in the caption always points to the URL written by the author, including a
timestamp or Vimeo privacy hash when present.

## Options

| Option | Default | Notes |
|---|---|---|
| `poster` | YouTube thumbnail | Static fallback image. **Required for Vimeo.** Prefer a committed local JPEG or PNG so exports do not need the network. |
| `video-title` | `YouTube video` / `Vimeo video` | Human-readable title used for the source link and default accessibility text. |
| `alt` | derived | Alternative text for the poster. Describe what the poster shows, not merely that it is a video. |
| `title` | `video-title` | Accessible title for the iframe. |
| `link-text` | `video-title` | Text of the source link. |
| `width` | `100%` | **Percentages only.** The theme mangles `px` values. |
| `aspect` | `16:9` | Other ratios need a matching rule in `../css/custom.css`. |
| `align` | `center` | `left`, `center`, `right`. |
| `label` | — | Makes the figure cross-referenceable. |
| `class` | — | Extra classes on the video frame. |
| `enumerated` | — | Whether the figure is numbered. |

## How the fallback works

The directive uses the same structural fallback as `{simulation}` and
`{animation}`: an `iframe` and a plain `image` are siblings in one figure.
The website hides the image; browser print hides the iframe; PDF and Word keep
the image after the export path drops the unsupported iframe. The caption's
ordinary link survives every format, so a reader can still open the video.

# The H5P plugin

An H5P activity a reader can use inline. Each chapter carries one five-question
review carousel after its Summary, mixing multiple choice, true/false,
drag-the-words, fill-in-the-blank, and mark-the-words, and some of them show a
chapter figure alongside the question. The loader and build pipeline accept any
H5P content type.

The content type is [H5P](https://h5p.org), but nothing about it depends on
h5p.com or on any other externally hosted service. Unpacked content and
standard `.h5p` packages live under `h5p/`; `scripts/prepare-h5p.mjs` follows
their dependency metadata and generates the shared runtime tree published by
the website. See [`../h5p/README.md`](../h5p/README.md) for the full layout and
for how to add an activity.

## Usage

````markdown
:::{h5p} ch01-chapter-review
:label: check:ch01-chapter-review
:title: Chapter 1 interactive review

1. **Multiple choice, from a figure.** The activity reproduces the anatomy-of-a-sinusoid figure from earlier in this chapter, which draws two sinusoids of equal amplitude and equal period. Which quantity distinguishes them: phase, amplitude, frequency, or period?
2. **True or false.** Doubling the amplitude of a vibrating string doubles the energy stored in the vibration.
3. **Fill in the blanks.** A steady tone at $250$ Hz has a period of ___ ms, because frequency and period are ___.
:::
````

A bare id resolves to `/h5p/embed.html?id=<id>`, which loads
`/h5p/content/<id>/` through the vendored player. The body is **required**: it
is not a caption, it is the fallback question text itself, shown instead of the
widget in every format that cannot run an iframe.

## Options

| Option | Default | Notes |
|---|---|---|
| `title` | derived | Accessible title for the iframe. |
| `width` | `100%` | **Percentages only.** The theme mangles `px` values. |
| `align` | `center` | `left`, `center`, `right`. |
| `label` | — | Makes the block cross-referenceable. |
| `class` | — | Extra classes on the exercise frame. |

There is no universal `aspect` option: H5P content types have very different
layouts. `css/custom.css` gives `.h5p-frame` a generous default height instead
of the theme's video-style aspect ratio. A content type needing more room can
use `:class:` with a corresponding project CSS rule.

## How the fallback works

The mechanism is the same as `{animation}`'s, with one difference: the
fallback is the directive's own body rather than necessarily being an image.
For a question, write out the question and choices ungraded; for another
content type, provide a useful static equivalent or description. Each
directive emits **both** an `iframe` node and the body as siblings inside one
container, and each renderer keeps whichever it understands:

| Output | `iframe` | fallback body | Result |
|---|---|---|---|
| HTML site | live exercise | hidden by `custom.css` | the exercise |
| Browser print | hidden by `@media print` | shown by `@media print` | the question, ungraded |
| `--pdf` / `--tex` | dropped by `export.mjs` | rendered normally | the question, ungraded |
| `--docx` | unsupported, skipped | rendered normally | the question, ungraded |
| `--md` | folded away | rendered normally | the question, ungraded |

A bare id resolves to a root-relative `/h5p/embed.html?...` URL rather than a
path relative to the source `.md` file, for the same reason `{animation}`'s
player URL is root-relative: MyST does not resolve a relative path written
into an `iframe` node the way it resolves one in a `link` or `image` node.
`project.static_files` in `myst.yml` declares the generated H5P tree to keep
that URL stable and unhashed, the same way it declares `audio` and
`animations`.

# The export plugin

`myst-to-tex` renders a fixed set of node types and reports anything else as
`Unhandled LaTeX conversion for node of "<type>"` — then drops it. Five of the
types this book leans on are not in that set:

| Node | Written as | Without the plugin |
|---|---|---|
| `exercise` | `:::{exercise}` | every chapter's Problems section vanishes |
| `solution` | `:::{solution}` | every worked solution vanishes |
| `aside` | `:::{margin}` | every margin note vanishes |
| `details` | `:::{dropdown}` | every optional derivation vanishes |
| `iframe` | simulation, animation, video, and H5P directives | intended — the sibling fallback carries it |

Since a plugin cannot supply a renderer, `export.mjs` rewrites those nodes into
ones the renderer already understands, and only while an export is being built.

Three things make that work, and each is easy to get wrong:

- **`stage: 'project'`.** Project-stage transforms run *after*
  `resolveReferencesTransform`, so every `enumerator` is already assigned
  ("4.1") and every cross-reference's link text is already resolved. The same
  transform at `document` stage would lose both.
- **Nothing may be boxed.** Worked solutions contain figures, and LaTeX cannot
  open a float inside `framed`, `minipage`, or any other box: it fails with
  *Not in outer par mode* and loses the figure, its caption, and every
  `{numref}` pointing at it. The template brackets exercises with plain spacing
  commands for exactly this reason.
- **No custom environment.** The same `.tex` feeds pandoc for the Word edition,
  and pandoc discards the entire body of an environment it does not know. Bare
  commands it cannot read are skipped harmlessly instead.

## Editions

Two environment variables steer it. Neither is set for `myst start` or
`myst build --html`, where the plugin returns immediately.

| Variable | Values | Effect |
|---|---|---|
| `MYST_PRINT` | `full`, `student` | Which edition. `student` drops all solutions. Unset means the website — the plugin does nothing. |
| `MYST_SITE_URL` | a base URL | Only for chapter offprints. An offprint holds one chapter, so its "see Chapter 7" references leave the file and point at the website. Leave unset for the whole book, where the jump should stay inside the PDF. |

[`../scripts/build-exports.sh`](../scripts/build-exports.sh) sets both correctly
for each artifact; prefer it to calling `myst build` by hand.
