/**
 * @fileoverview MyST plugin for embedding audio examples.
 *
 * A book about music has to be able to show its examples and let a reader hear
 * them. This directive builds the figure that does both.
 *
 * **Why there is no inline player.** The obvious implementation is an
 * `<audio controls>` element, and it does not survive. MyST parses raw HTML at
 * the document stage, converts what it can to mdast, and drops the rest;
 * `<audio>` has no mdast equivalent and is removed outright, leaving nothing on
 * the page. (`<div>` survives, `<iframe>` survives as an `iframe` node, and
 * mystmd 1.10.1 has no `{video}` or `{audio}` directive of its own.) Routing a
 * player through an `iframe` fails for a different reason: MyST content-hashes
 * and copies a locally linked media file and rewrites the URL, so the hashed
 * path the clip actually lands on is not knowable when the directive runs, and
 * an iframe `src` is never processed that way.
 *
 * So the figure is built from nodes MyST renders natively, and the reader
 * listens by following a link, which is also what the two music-theory books in
 * this fleet do. What the plugin adds over a bare link is the part that carries
 * the physics: the waveform-and-spectrum figure that shows what is in the clip,
 * a transcript for readers who cannot hear it, and one consistent, numbered,
 * cross-referenceable figure in every output format.
 *
 *   HTML site   the figure, with a link per clip under it
 *   PDF, DOCX   the same figure and caption; the link prints as a URL
 *
 * Clips are generated, not sampled: `scripts/audio/*.py` synthesizes each one
 * and writes the matching figure beside it, so every example is reproducible
 * and carries no third-party licence.
 *
 * @module plugins/audio
 * @see {@link https://mystmd.org/guide/javascript-plugins}
 */

/**
 * Directory holding the generated clips, relative to the project root.
 *
 * The leading slash matters: MyST resolves a `/`-prefixed URL against the
 * project root rather than the directory of the source file, and the directive
 * has no way to know which file it was written in.
 *
 * @type {string}
 */
const AUDIO_ROOT = '/audio';

/**
 * Directory holding the static figure that stands in for a clip in print.
 *
 * @type {string}
 */
const IMAGE_ROOT = '/images';

/**
 * File extension of the generated clips.
 *
 * MP3 rather than WAV: the clips are committed to the repository, and a
 * two-second stereo WAV is roughly twenty times the size of the MP3 that
 * `scripts/audio/render.py` writes from it. Every browser in use plays MP3.
 *
 * @type {string}
 */
const AUDIO_EXTENSION = '.mp3';

/**
 * Words left lowercase when title-casing a slug, unless they lead the name.
 *
 * @type {Set<string>}
 */
const MINOR_WORDS = new Set( [ 'a', 'an', 'and', 'as', 'at', 'by', 'for', 'in', 'of', 'on', 'or', 'the', 'to', 'vs' ] );

/**
 * Turns `ch05-sawtooth-vs-square` into `Sawtooth vs Square`.
 *
 * The chapter prefix is dropped: it disambiguates the file on disk, not the
 * example on the page.
 *
 * @param {string} id - A clip id.
 * @returns {string} A human-readable name.
 */
export function humanize( id ) {
  return String( id )
    .replace( /^ch\d{2}[-_]/, '' )
    .replace( /[-_]+/g, ' ' )
    .replace( /([a-z0-9])([A-Z])/g, '$1 $2' )
    .replace( /\s+/g, ' ' )
    .trim()
    .split( ' ' )
    .map( ( word, index ) => {
      if ( index > 0 && MINOR_WORDS.has( word.toLowerCase() ) ) {
        return word.toLowerCase();
      }
      return /[A-Z]/.test( word ) ? word : word.charAt( 0 ).toUpperCase() + word.slice( 1 );
    } )
    .join( ' ' );
}

/**
 * Resolves one clip reference to a URL.
 *
 * A bare id names a generated clip in `/audio`; anything that looks like a path
 * or a URL is passed through untouched, so an externally hosted example works
 * without a new provider mechanism.
 *
 * @param {string} reference - A clip id, a path, or a URL.
 * @returns {{url: string, id: string, isBare: boolean}}
 */
export function resolveClip( reference ) {
  const value = String( reference ).trim();
  if ( /^https?:\/\//i.test( value ) || value.startsWith( '/' ) || value.startsWith( '.' ) ) {
    const id = value.split( '/' ).pop().replace( /\.[a-z0-9]+$/i, '' );
    return { url: value, id, isBare: false };
  }
  const id = value.replace( /\.[a-z0-9]+$/i, '' );
  const extension = /\.[a-z0-9]+$/i.test( value ) ? '' : AUDIO_EXTENSION;
  return { url: `${ AUDIO_ROOT }/${ value }${ extension }`, id, isBare: true };
}

/**
 * Splits a comma-separated directive option into trimmed, non-empty parts.
 *
 * @param {(string|undefined)} value - The raw option value.
 * @returns {Array<string>} The parts.
 */
export function splitList( value ) {
  return String( value ?? '' )
    .split( ',' )
    .map( part => part.trim() )
    .filter( Boolean );
}

/**
 * Builds a paragraph node reporting a directive error.
 *
 * The message is also pushed onto the vfile so it appears in the build log
 * rather than only in the rendered output.
 *
 * @param {string} message - What went wrong.
 * @param {Object} [vfile] - The vfile MyST passes to `run`.
 * @returns {Array<Object>} A single-paragraph AST.
 */
function directiveError( message, vfile ) {
  if ( vfile && typeof vfile.message === 'function' ) {
    const reported = vfile.message( message );
    reported.fatal = false;
    reported.source = 'plugins/audio.mjs';
  }
  return [ {
    type: 'paragraph',
    children: [ { type: 'strong', children: [ { type: 'text', value: `Audio error: ${ message }` } ] } ]
  } ];
}

/**
 * Implementation behind `{audio}`.
 *
 * @param {Object} data - Directive data supplied by MyST.
 * @param {Object} vfile - The vfile for the source document.
 * @returns {Array<Object>} The AST nodes to insert.
 */
function runAudio( data, vfile ) {
  const options = data.options ?? {};

  if ( !data.arg ) {
    return directiveError( 'an audio clip id, path, or URL is required', vfile );
  }

  const references = splitList( data.arg );
  if ( !references.length ) {
    return directiveError( 'an audio clip id, path, or URL is required', vfile );
  }

  const names = splitList( options.names );
  if ( names.length && names.length !== references.length ) {
    return directiveError(
      `:names: has ${ names.length } entries but the directive names ${ references.length } clips`,
      vfile
    );
  }

  const clips = references.map( ( reference, index ) => {
    const { url, id } = resolveClip( reference );
    return { url, id, name: names[ index ] || humanize( id ) };
  } );

  // The figure that stands in for the player everywhere the player cannot go.
  // By convention each generator writes `images/<id>.svg` beside its clip, so
  // the single-clip case needs no `:figure:` at all; a comparison of several
  // clips is one picture and has to name it.
  let figureUrl = options.figure;
  if ( !figureUrl && !options[ 'no-figure' ] ) {
    if ( clips.length === 1 && resolveClip( references[ 0 ] ).isBare ) {
      figureUrl = `${ IMAGE_ROOT }/${ clips[ 0 ].id }.svg`;
    }
    else {
      return directiveError(
        'several clips share one figure, so `:figure:` must name it ' +
        '(or pass `:no-figure:`)',
        vfile
      );
    }
  }

  const listed = clips.map( clip => clip.name ).join( ', ' );
  const children = [];

  // The figure. Shown in every format, including on the website: a reader who
  // has not pressed play yet should still be able to see what is in the clip,
  // and a reader who cannot hear it gets the whole point from the picture and
  // the transcript.
  if ( figureUrl ) {
    children.push( {
      type: 'image',
      url: figureUrl,
      alt: options.alt || `Waveform and spectrum of ${ listed }`,
      width: options.width || '100%',
      align: options.align || 'center',
      class: 'audio-figure'
    } );
  }

  // The caption: the author's body, then what a reader who cannot hear the clip
  // needs, then the link that survives every format.
  const captionChildren = [ ...( data.body ?? [] ) ];

  if ( options.transcript ) {
    captionChildren.push( {
      type: 'paragraph',
      class: 'audio-transcript',
      children: [
        { type: 'emphasis', children: [ { type: 'text', value: 'What you hear: ' } ] },
        { type: 'text', value: String( options.transcript ).trim() }
      ]
    } );
  }

  if ( !options[ 'no-link' ] ) {
    const linkChildren = [ { type: 'text', value: clips.length > 1 ? 'Listen: ' : 'Listen: ' } ];
    clips.forEach( ( clip, index ) => {
      if ( index ) {
        linkChildren.push( { type: 'text', value: ', ' } );
      }
      linkChildren.push( {
        type: 'link',
        url: clip.url,
        children: [ { type: 'text', value: clips.length === 1 ? ( options[ 'link-text' ] || clip.name ) : clip.name } ]
      } );
    } );
    captionChildren.push( { type: 'paragraph', class: 'audio-link', children: linkChildren } );
  }

  if ( captionChildren.length ) {
    children.push( { type: 'caption', children: captionChildren } );
  }

  const container = {
    type: 'container',
    kind: 'figure',
    class: 'audio',
    // Without this, the player and the fallback image are lettered (a) and (b)
    // as subfigures.
    noSubcontainers: true,
    children
  };

  if ( options.label ) {
    const label = String( options.label ).trim();
    container.label = label;
    container.identifier = label.toLowerCase();
  }
  if ( typeof options.enumerated === 'boolean' ) {
    container.enumerated = options.enumerated;
  }

  return [ container ];
}

/**
 * @type {Object} A MyST directive spec.
 */
const audioDirective = {
  name: 'audio',
  alias: [ 'sound' ],
  doc: 'Embed one or more audio examples, with a waveform or spectrum figure for ' +
       'PDF, DOCX, Markdown, and print.',
  arg: {
    type: String,
    required: true,
    doc: 'A clip id such as `ch05-sawtooth`, resolved to `/audio/<id>.mp3`; a ' +
         'path or URL to an audio file; or a comma-separated list of either, to ' +
         'put several players in one figure.'
  },
  options: {
    figure: {
      type: String,
      doc: 'Static figure shown in PDF, DOCX, Markdown, and print. Relative to ' +
           'the source file, `/`-prefixed for the project root, or a URL. ' +
           'Defaults to `/images/<id>.svg` for a single generated clip; required ' +
           'when the directive names several.'
    },
    'no-figure': {
      type: Boolean,
      doc: 'Omit the static fallback figure entirely.'
    },
    names: {
      type: String,
      doc: 'Comma-separated labels for the players, one per clip. Defaults to ' +
           'each clip id made readable.'
    },
    transcript: {
      type: String,
      doc: 'One sentence describing what the clip sounds like, for readers who ' +
           'cannot hear it and for every printed format. Strongly recommended.'
    },
    alt: {
      type: String,
      doc: 'Alternative text for the fallback figure.'
    },
    width: {
      type: String,
      doc: 'Width of the fallback figure, e.g. `80%` (default `100%`).'
    },
    align: {
      type: String,
      doc: 'One of `left`, `center` (default), or `right`.'
    },
    label: {
      type: String,
      doc: 'Label the figure so it can be cross-referenced, e.g. `fig:ch05-timbre-audio`.'
    },
    class: {
      type: String,
      doc: 'Extra space-delimited CSS classes for the player.'
    },
    enumerated: {
      type: Boolean,
      doc: 'Whether the figure is numbered.'
    },
    'link-text': {
      type: String,
      doc: 'Text of the caption link to the clip. Defaults to the clip name.'
    },
    'no-link': {
      type: Boolean,
      doc: 'Suppress the caption link to the clip.'
    }
  },
  body: { type: 'myst', doc: 'Caption for the audio example.' },
  /**
   * @param {Object} data - Directive data supplied by MyST.
   * @param {Object} vfile - The vfile for the source document.
   * @returns {Array<Object>} The AST nodes to insert.
   */
  run( data, vfile ) {
    return runAudio( data, vfile );
  }
};

/**
 * @type {{name: string, directives: Array<Object>}}
 */
const plugin = {
  name: 'Audio examples',
  directives: [ audioDirective ]
};

export default plugin;
