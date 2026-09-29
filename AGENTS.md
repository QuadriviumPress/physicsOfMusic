# AGENTS.md

## Standard

This book follows the [QuadriviumPress MyST baseline](https://github.com/QuadriviumPress/bindery/blob/main/doc/myst-baseline.md) and the [presentation skill](https://github.com/QuadriviumPress/bindery/blob/main/skills/quadrivium-myst-presentation/SKILL.md).

## Commands

```bash
npm run check:toolchain
npm run h5p:check
npm run h5p:generate
npm run h5p:prepare
npm run prestart
npm run start
npm run prebuild
npm run build
npm run precheck
npm run verify
npm run check
npm run check:figures
npm run check:project
npm run test
npm run test:exports
npm run build:exports
npm run build:pdf
npm run build:chapters
npm run build:docx
npm run audio:check
npm run audio:render
npm run notation:check
npm run notation:render
```

`npm run check` is the production-equivalent verification and HTML build.

## Intentional differences

- `start`, `build`, and `check` invoke MyST through `scripts/run-myst.mjs`. That launcher works around the npm-version probe bundled with older MyST releases. It stays in place after the pin move to `mystmd@1.11.0`.
- `check:toolchain`, `h5p:check`, `h5p:generate`, and `h5p:prepare` support H5P. `verify` runs the H5P check before prepare.
- `verify` also runs the project validator and `npm test`.
- Notation and audio scripts: `notation:render`, `notation:check`, `audio:render`, `audio:check`.
- Print exports: `build:exports`, `build:pdf`, `build:chapters`, `build:docx`, plus `test:exports` and `check:figures`.
- `devDependencies` also includes `fflate`, `jsdom`, and `vexflow`.
- `scripts/setup-pwa.mjs` deletes the duplicate `/build/h5p` copy and marks H5P iframes `loading="lazy"`.

## Presentation gap

Problems already use `{exercise}` and `{solution}` dropdowns. Fences are colon-style (`:::`) and labels use hyphens (`ex-…`) rather than the backtick fences and `ex:` labels in the presentation skill. Fence and label alignment is deferred.
