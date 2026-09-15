#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { parse } from 'yaml';

export function chapterLists(source) {
  const project = parse(source).project;
  const chapters = entries => (entries ?? []).flatMap(entry => [
    ...(entry.file?.startsWith('chapters/') ? [entry.file] : []),
    ...chapters(entry.children),
  ]);
  return {
    toc: chapters(project.toc),
    exports: chapters(project.exports?.find(entry => entry.id === 'book')?.articles),
  };
}

// Track nested directives and ordinary code fences, including MyST's colon
// fences. Examples inside ordinary code blocks are not actual figures.
export function figuresWithoutAlt(source) {
  const stack = [];
  const missing = [];
  for (const line of source.split(/\r?\n/)) {
    const match = /^ {0,3}(`{3,}|~{3,}|:{3,})(.*)$/.exec(line);
    const top = stack.at(-1);
    if (match) {
      const [, fence, rest] = match;
      if (top && !rest.trim() && fence[0] === top.char && fence.length >= top.length) {
        stack.pop();
        if (top.figure && !top.alt) missing.push(top.figure);
      } else if (!top?.code) {
        const directive = /^\s*\{([^}]+)\}\s*(.*)$/.exec(rest);
        if (rest.trim() || fence[0] !== ':') stack.push({
          char: fence[0], length: fence.length,
          code: !directive, figure: directive?.[1] === 'figure' ? directive[2] : null,
          alt: false,
        });
      }
    } else if (top?.figure && /^\s*:alt:\s*\S+/.test(line)) {
      top.alt = true;
    }
  }
  for (const entry of stack) if (entry.figure && !entry.alt) missing.push(entry.figure);
  return missing;
}

/**
 * Extracts and parses a page's YAML frontmatter.
 *
 * This exists because MyST fails a malformed frontmatter block *silently*: the
 * page still builds, but none of its metadata takes effect, so its `label:`
 * never registers and every cross-reference to the chapter dangles. The
 * original instance was a chapter titled `Percussion: Membranes, Bars, and
 * Plates`, where the unquoted colon made the line something other than a YAML
 * scalar.
 *
 * @param {string} source - The full text of a Markdown file.
 * @returns {{ok: boolean, data: (Object|null), error: (string|null)}}
 */
export function frontmatter( source ) {
  const match = /^---\r?\n([\s\S]*?)\r?\n---\r?\n/.exec( source );
  if ( !match ) {
    return { ok: false, data: null, error: 'no YAML frontmatter block' };
  }
  try {
    return { ok: true, data: parse( match[ 1 ] ) ?? {}, error: null };
  }
  catch ( error ) {
    return { ok: false, data: null, error: String( error.message ?? error ).split( '\n' )[ 0 ] };
  }
}

/**
 * Every clip and figure an `{audio}` directive names.
 *
 * The directive takes a comma-separated argument and an optional `:figure:`,
 * and defaults the figure to `/images/<id>.svg`. A missing clip is invisible on
 * the website -- the player simply does nothing when pressed -- so it has to be
 * caught here.
 *
 * @param {string} source - The full text of a Markdown file.
 * @returns {Array<{clips: Array<string>, figure: (string|null), noFigure: boolean}>}
 */
export function audioDirectives( source ) {
  const found = [];
  const pattern = /^\s*(?:```|:::)+\{audio\}\s*(.+)$/gm;
  for ( const match of source.matchAll( pattern ) ) {
    const rest = source.slice( match.index + match[ 0 ].length );
    const body = rest.split( /\n(?=\s*\S)/ );
    const options = ( body[ 0 ] ?? '' ) + '\n' + rest.split( /\n\s*\n/ )[ 0 ];
    found.push( {
      clips: match[ 1 ].split( ',' ).map( part => part.trim() ).filter( Boolean ),
      figure: /^\s*:figure:\s*(\S+)/m.exec( options )?.[ 1 ] ?? null,
      noFigure: /^\s*:no-figure:/m.test( options )
    } );
  }
  return found;
}

function main() {
  const root = path.resolve(import.meta.dirname, '..');
  const config = fs.readFileSync(path.join(root, 'myst.yml'), 'utf8');
  const failures = [];
  const lists = chapterLists(config);
  const tocChapters = lists.toc;
  const chapterFiles = fs.readdirSync(path.join(root, 'chapters'))
    .filter(name => /^ch-\d{2}-.+\.md$/.test(name))
    .sort()
    .map(name => `chapters/${name}`);
  const exportChapters = lists.exports;

  if (JSON.stringify(tocChapters) !== JSON.stringify(chapterFiles)) {
    failures.push(`website TOC chapters differ from the chapter directory\n` +
      `  expected ${JSON.stringify(chapterFiles)}\n  found    ${JSON.stringify(tocChapters)}`);
  }
  if (JSON.stringify(exportChapters) !== JSON.stringify(chapterFiles)) {
    failures.push(`print export chapters differ from the chapter directory\n` +
      `  expected ${JSON.stringify(chapterFiles)}\n  found    ${JSON.stringify(exportChapters)}`);
  }

  const labels = new Map();
  const chapterLabels = new Map();
  for (const relative of fs.readdirSync(path.join(root, 'chapters')).filter(name => name.endsWith('.md'))) {
    const file = path.join('chapters', relative);
    const source = fs.readFileSync(path.join(root, file), 'utf8');

    // MyST accepts a malformed frontmatter block without complaint and then
    // ignores every key in it, so check it here rather than trusting the build.
    const front = frontmatter( source );
    if ( !front.ok ) {
      failures.push( `${file}: frontmatter does not parse (${front.error}). ` +
        'A title containing a colon must be quoted.' );
    }
    else {
      const number = Number( relative.slice( 3, 5 ) );
      for ( const key of [ 'title', 'short_title', 'label' ] ) {
        if ( !front.data[ key ] ) failures.push( `${file}: frontmatter has no \`${key}\`` );
      }
      const enumerator = front.data.numbering?.enumerator;
      if ( enumerator !== `${number}.%s` ) {
        failures.push( `${file}: numbering.enumerator is ${JSON.stringify( enumerator )}, expected "${number}.%s"` );
      }
      if ( front.data.short_title && !String( front.data.short_title ).startsWith( `Chapter ${number}.` ) ) {
        failures.push( `${file}: short_title should start "Chapter ${number}."` );
      }
      const chapterLabel = front.data.label;
      if ( chapterLabel ) {
        if ( chapterLabels.has( chapterLabel ) ) {
          failures.push( `duplicate chapter label ${chapterLabel}: ${chapterLabels.get( chapterLabel )} and ${file}` );
        }
        chapterLabels.set( chapterLabel, file );
      }
    }

    // An {audio} clip that does not exist fails silently too: the player
    // renders and does nothing when pressed.
    for ( const directive of audioDirectives( source ) ) {
      for ( const clip of directive.clips ) {
        if ( /^https?:/.test( clip ) ) continue;
        const name = clip.includes( '.' ) ? clip : `${clip}.mp3`;
        const target = clip.startsWith( '/' ) || clip.startsWith( '.' )
                       ? path.resolve( path.dirname( path.join( root, file ) ), name.replace( /^\//, '' ) )
                       : path.join( root, 'audio', name );
        if ( !fs.existsSync( target ) ) failures.push( `${file}: audio clip ${clip} is missing (${path.relative( root, target )})` );
      }
      if ( directive.noFigure ) continue;
      const figure = directive.figure
                     ?? ( directive.clips.length === 1 ? `/images/${directive.clips[ 0 ]}.svg` : null );
      if ( !figure ) continue;
      const target = figure.startsWith( '/' )
                     ? path.join( root, figure.slice( 1 ) )
                     : path.resolve( path.dirname( path.join( root, file ) ), figure );
      if ( !/^https?:/.test( figure ) && !fs.existsSync( target ) ) {
        failures.push( `${file}: audio figure ${figure} is missing (${path.relative( root, target )})` );
      }
    }
    for (const [, label] of source.matchAll(/^:(?:label|name):\s*(\S+)/gm)) {
      if (labels.has(label)) failures.push(`duplicate label ${label}: ${labels.get(label)} and ${file}`);
      labels.set(label, file);
    }
    for (const figure of figuresWithoutAlt(source)) {
      failures.push(`${file}: figure ${figure} has no :alt:`);
    }
  }

  if (failures.length) {
    console.error(failures.map(item => `ERROR: ${item}`).join('\n'));
    process.exit(1);
  }
  console.log(`Project metadata valid: ${chapterFiles.length} chapters, ${chapterLabels.size} chapter labels, ${labels.size} directive labels.`);
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) main();
