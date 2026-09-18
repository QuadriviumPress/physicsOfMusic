/**
 * @fileoverview MyST plugin for embedding the book's own self-hosted H5P
 * exercises: short, auto-graded, multiple-choice "check your understanding"
 * questions, one per concept, that a reader can answer on the website.
 *
 * H5P content is not authored through h5p.com or any other external service;
 * it is a set of static files vendored into `h5p/` (library code fetched once
 * via the `h5p` CLI, content authored by hand as `content.json`) and played
 * client-side by the `h5p-standalone` runtime, also vendored there. There is
 * no server and no database, matching how `plugins/audio.mjs` and
 * `plugins/animation.mjs` self-host their own media. See `h5p/README.md` for
 * how to add a new question.
 *
 * A multiple-choice widget has no static image worth showing in a PDF, DOCX,
 * or Markdown export, so the fallback is not a screenshot but the question
 * itself, written out as the directive's body and rendered as ordinary prose
 * and a lettered list -- exactly what a print reader needs to attempt the
 * question, without the auto-grading. The mechanism is the same
 * iframe-plus-sibling one `plugins/simulation.mjs` and `plugins/animation.mjs`
 * use: MyST's `iframe` node is rendered by the site theme and nothing else, so
 * `css/custom.css` hides the fallback on the website and hides the iframe
 * everywhere else can only render it.
 *
 * @module plugins/h5p
 * @see {@link https://mystmd.org/guide/javascript-plugins}
 */

/**
 * Root the H5P content is served from. `project.static_files` in `myst.yml`
 * copies `h5p/` there verbatim, alongside `audio/` and `animations/`.
 *
 * The leading slash matters: MyST resolves a `/`-prefixed image or iframe URL
 * against the project root rather than the directory of the source file, and
 * the directive has no way to know which file it was written in.
 *
 * @type {string}
 */
const rawBaseUrl = process.env.BASE_URL || '/';
const SITE_ROOT = rawBaseUrl === '/'
  ? ''
  : `/${ rawBaseUrl.replace( /^\/+|\/+$/g, '' ) }`;
const H5P_ROOT = `${ SITE_ROOT }/h5p`;

/**
 * Words left lowercase when title-casing a slug, unless they lead the name.
 *
 * @type {Set<string>}
 */
const MINOR_WORDS = new Set( [ 'a', 'an', 'and', 'as', 'at', 'by', 'for', 'in', 'of', 'on', 'or', 'the', 'to', 'vs' ] );

/**
 * Turns `ch01-hookes-law-generality` into `Hooke's Law Generality`-ish title
 * case, good enough for an iframe's accessible title.
 *
 * The chapter prefix is dropped: it disambiguates the content folder on disk,
 * not the question on the page.
 *
 * @param {string} id
 * @returns {string}
 */
function humanize( id ) {
  const words = String( id )
    .replace( /^ch\d{2}[-_]/, '' )
    .replace( /[-_]+/g, ' ' )
    .trim()
    .split( ' ' );
  return words
    .map( ( word, index ) => {
      if ( index > 0 && MINOR_WORDS.has( word.toLowerCase() ) ) {
        return word.toLowerCase();
      }
      return word.charAt( 0 ).toUpperCase() + word.slice( 1 );
    } )
    .join( ' ' );
}

/**
 * Resolves one directive argument to an H5P embed URL.
 *
 * A bare id names a folder in `h5p/content/` (e.g. `ch01-vacuum-medium`
 * resolves to `/h5p/embed.html?id=ch01-vacuum-medium`); anything that already
 * looks like a path or a URL is passed through untouched, for an H5P instance
 * hosted somewhere else.
 *
 * @param {string} arg - The directive argument.
 * @returns {string}
 */
function resolveEmbedUrl( arg ) {
  const value = String( arg ).trim();
  if ( /^https?:\/\//i.test( value ) || value.startsWith( '/' ) || value.startsWith( '.' ) ) {
    return value;
  }
  return `${ H5P_ROOT }/embed.html?id=${ encodeURIComponent( value ) }`;
}

/**
 * Builds a paragraph node reporting a directive error.
 *
 * @param {string} message
 * @param {Object} [vfile]
 * @returns {Array<Object>}
 */
function directiveError( message, vfile ) {
  if ( vfile && typeof vfile.message === 'function' ) {
    const reported = vfile.message( message );
    reported.fatal = false;
    reported.source = 'plugins/h5p.mjs';
  }
  return [ {
    type: 'paragraph',
    children: [ { type: 'strong', children: [ { type: 'text', value: `H5P error: ${ message }` } ] } ]
  } ];
}

/**
 * Implementation behind `{h5p}`.
 *
 * @param {Object} data - Directive data supplied by MyST.
 * @param {Object} vfile - The vfile for the source document.
 * @returns {Array<Object>} The AST nodes to insert.
 */
function runH5p( data, vfile ) {
  const options = data.options ?? {};

  if ( !data.arg ) {
    return directiveError( 'an H5P content id, path, or URL is required', vfile );
  }

  if ( !data.body || data.body.length === 0 ) {
    return directiveError(
      'a body is required: write out the question and its choices, which doubles as ' +
      'the fallback for print, PDF, DOCX, and Markdown, where the interactive widget cannot appear',
      vfile
    );
  }

  const id = String( data.arg ).trim();
  const url = resolveEmbedUrl( id );
  const name = humanize( id );

  const width = options.width || '100%';
  const title = options.title || `Check your understanding — ${ name }`;
  const align = options.align || 'center';

  const children = [
    // The live exercise. Rendered by the site theme and by nothing else; see
    // the fallback table in plugins/simulation.mjs and the module comment above.
    {
      type: 'iframe',
      src: url,
      width,
      align,
      title,
      class: [ 'h5p-frame', options.class ].filter( Boolean ).join( ' ' )
    },
    // The static fallback, for PDF, DOCX, Markdown, and print: the question
    // itself, ungraded. Not marked `placeholder: true`; see plugins/simulation.mjs
    // for why that particular shortcut does not apply here either.
    {
      type: 'div',
      class: 'h5p-fallback',
      children: [ ...data.body ]
    }
  ];

  // A plain `div`, not a `container`: MyST's container validation only
  // accepts a fixed whitelist of content types (image, iframe, table, code,
  // cards, ...) as a container's non-caption children, and the fallback body
  // here is ordinary prose and a list, which is not on that whitelist.
  // `export.mjs` already builds the same kind of node for exercises and
  // solutions for exactly this reason.
  const wrapper = {
    type: 'div',
    class: [ 'h5p', options.class ].filter( Boolean ).join( ' ' ),
    children
  };

  if ( options.label ) {
    const label = String( options.label ).trim();
    wrapper.label = label;
    wrapper.identifier = label.toLowerCase();
  }

  return [ wrapper ];
}

const h5pDirective = {
  name: 'h5p',
  doc: 'Embed one of the book\'s own self-hosted H5P exercises from `h5p/content/`, with the ' +
       'question written out as the directive body as the fallback for print, PDF, DOCX, and Markdown.',
  arg: {
    type: String,
    required: true,
    doc: 'The H5P content id (e.g. `ch01-vacuum-medium`, resolving to ' +
         '`h5p/content/ch01-vacuum-medium/`), or a path or URL to an H5P instance hosted elsewhere.'
  },
  options: {
    title: {
      type: String,
      doc: 'Accessible title for the iframe. Defaults to "Check your understanding — <name>".'
    },
    width: {
      type: String,
      doc: 'Width of the exercise as a percentage, e.g. `80%` (default `100%`).'
    },
    align: {
      type: String,
      doc: 'One of `left`, `center` (default), or `right`.'
    },
    label: {
      type: String,
      doc: 'Label the block so it can be cross-referenced, e.g. `check:ch01-vacuum-medium`.'
    },
    class: {
      type: String,
      doc: 'Extra space-delimited CSS classes for the exercise frame.'
    }
  },
  body: {
    type: 'myst',
    required: true,
    doc: 'The question and its choices, written out in Markdown. Required: this is what print, ' +
         'PDF, DOCX, and Markdown readers see instead of the interactive widget.'
  },
  /**
   * @param {Object} data - Directive data supplied by MyST.
   * @param {Object} vfile - The vfile for the source document.
   * @returns {Array<Object>} The AST nodes to insert.
   */
  run( data, vfile ) {
    return runH5p( data, vfile );
  }
};

/**
 * @type {{name: string, directives: Array<Object>}}
 */
const plugin = {
  name: 'H5P exercises',
  directives: [ h5pDirective ]
};

export default plugin;
