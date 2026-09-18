# Self-hosted H5P exercises

Static files only. No h5p.com account, no self-hosted H5P server (WordPress,
Drupal, Moodle), no database. A question is a folder of JSON; the player is a
vendored JavaScript library; `embed.html` glues the two together in an iframe.
`plugins/h5p.mjs` documents the MyST-facing side of this; this file documents
the content itself.

```
h5p/
  embed.html       generic loader: reads ?id=<content-id> from its own URL
  player/           vendored h5p-standalone runtime (the H5P core, as a client-side player)
  libraries/        vendored H5P.MultiChoice and its dependencies (shared by every question)
  content/
    <id>/
      h5p.json       content metadata: title, main library, dependency versions
      content/
        content.json  the question text and answer choices
```

`myst.yml`'s `project.static_files` copies this whole tree to the site root
verbatim, so it is always reachable at `/h5p/...` regardless of where a chapter
page that embeds it lives.

## Why this layout

[`h5p-standalone`](https://github.com/tunapanda/h5p-standalone) plays H5P
content without a server, but it still needs the actual content-type code
(`H5P.MultiChoice`, `H5P.Question`, `H5P.JoubelUI`, …) — the same libraries a
real H5P installation downloads from the H5P Hub when an author adds that
content type. Vendoring one copy of them under `libraries/` and pointing every
question at it with `librariesPath` (rather than duplicating them inside each
`content/<id>/`) is what keeps 15 questions costing kilobytes each instead of
several megabytes each.

## Adding a question

1. Pick an id, e.g. `ch04-quality-factor`, matching the chapter it belongs to.
2. Create `content/<id>/h5p.json`:

   ```json
   {
     "title": "A short human-readable title",
     "language": "en",
     "mainLibrary": "H5P.MultiChoice",
     "embedTypes": ["iframe"],
     "license": "CC BY-NC-SA",
     "licenseVersion": "4.0",
     "preloadedDependencies": [
       { "machineName": "jQuery.ui", "majorVersion": 1, "minorVersion": 10 },
       { "machineName": "H5P.Components", "majorVersion": 1, "minorVersion": 0 },
       { "machineName": "H5P.Transition", "majorVersion": 1, "minorVersion": 0 },
       { "machineName": "H5P.FontIcons", "majorVersion": 1, "minorVersion": 0 },
       { "machineName": "FontAwesome", "majorVersion": 4, "minorVersion": 5 },
       { "machineName": "H5P.JoubelUI", "majorVersion": 1, "minorVersion": 3 },
       { "machineName": "H5P.Question", "majorVersion": 1, "minorVersion": 5 },
       { "machineName": "H5P.MultiChoice", "majorVersion": 1, "minorVersion": 16 }
     ]
   }
   ```

   This block of `preloadedDependencies` is the same for every question here —
   it is the full, flattened set of libraries `H5P.MultiChoice` needs, and it
   has to match what is actually present under `libraries/`.

3. Create `content/<id>/content/content.json`:

   ```json
   {
     "question": "<p>Question text, as HTML.</p>",
     "answers": [
       { "text": "<div>Correct choice</div>", "correct": true },
       { "text": "<div>Distractor</div>", "correct": false }
     ],
     "behaviour": {
       "enableRetry": true,
       "enableSolutionsButton": true,
       "singlePoint": true,
       "randomAnswers": true,
       "showSolutionsRequiresInput": true,
       "autoCheck": false,
       "passPercentage": 100,
       "showScorePoints": true
     }
   }
   ```

   Only `question` and `answers` are read by `H5P.MultiChoice` itself; every
   other field (`behaviour`, the button labels, …) has a built-in English
   default, kept explicit here only where it differs from that default.

4. Reference it from a chapter with `{h5p}` (see `../plugins/README.md`),
   writing the same question and choices into the directive body — that text
   is what print, PDF, DOCX, and Markdown readers see, so it has to say the
   same thing `content.json` does, even though nothing enforces that
   automatically.

5. Run `myst start`, open the chapter, and check the question renders and the
   "Check" button grades it correctly before committing.

## Where the vendored code came from

- `player/` is the `dist/` folder of `h5p-standalone@3.8.2`
  (`npm view h5p-standalone version` to check for a newer one; re-copy
  `node_modules/h5p-standalone/dist/` over `player/` to update it).
- `libraries/` was fetched with the official
  [`h5p-cli`](https://github.com/h5p/h5p-cli) toolkit, which clones each
  content type and its dependencies straight from the `h5p` GitHub
  organization (`h5p core && h5p setup h5p-multi-choice`), then exported and
  extracted to strip everything but the runtime files. Only the libraries
  `H5P.MultiChoice` needs to *run* are kept — no editor-only libraries, and
  none of the optional image/video/audio question-media libraries, since none
  of these questions use media. Adding a content type that does (or a
  different question type, e.g. `H5P.TrueFalse`) means repeating that fetch
  for the new library and adding its dependency set to `h5p.json`.

| Library | Version |
|---|---|
| H5P.MultiChoice | 1.16 |
| H5P.Question | 1.5 |
| H5P.JoubelUI | 1.3 |
| H5P.Components | 1.0 |
| H5P.Transition | 1.0 |
| H5P.FontIcons | 1.0 |
| FontAwesome | 4.5 |
| jQuery.ui | 1.10 |
