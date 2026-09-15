import { drawStave } from '../figure-helpers.mjs';

/**
 * The harmonic series on C2, partials 1-16, with each partial's departure from
 * equal temperament in cents.
 *
 * This is the figure the rest of the book keeps pointing back at. The two rows
 * are one series, split only because sixteen partials of C2 span four octaves
 * and will not fit legibly on one stave: partials 1-8 on the bass stave,
 * 9-16 on the treble.
 *
 * The cent figures are exact: partial n lies 1200*log2(n / 2^floor(log2 n))
 * cents above the equal-tempered note nearest it. They are what makes the point
 * -- the octaves and fifths are within two cents of the piano, the seventh
 * partial is a third of a semitone flat, and the eleventh sits almost exactly
 * between two keys.
 */

// key, displayed accidental, harmonic number, cents from equal temperament.
const LOWER = [
  [ 'c/2', null, 1, 0 ],
  [ 'c/3', null, 2, 0 ],
  [ 'g/3', null, 3, +2 ],
  [ 'c/4', null, 4, 0 ],
  [ 'e/4', null, 5, -14 ],
  [ 'g/4', null, 6, +2 ],
  [ 'bb/4', 'b', 7, -31 ],
  [ 'c/5', null, 8, 0 ]
];

const UPPER = [
  [ 'd/5', null, 9, +4 ],
  [ 'e/5', null, 10, -14 ],
  [ 'f#/5', '#', 11, +49 ],
  [ 'g/5', null, 12, +2 ],
  [ 'ab/5', 'b', 13, +41 ],
  [ 'bb/5', 'b', 14, -31 ],
  [ 'b/5', 'n', 15, -12 ],
  [ 'c/6', null, 16, 0 ]
];

/**
 * One row of the series, plus the harmonic numbers and cent deviations beneath.
 *
 * @param {Object} context - VexFlow rendering context.
 * @param {Object} overlay - SVG overlay helper from scripts/render-notation.mjs.
 * @param {Object} VF - The VexFlow module.
 * @param {Array} entries - Rows of `[key, accidental, harmonic, cents]`.
 * @param {number} y - Vertical position of the stave.
 * @param {string} clef - Clef name.
 */
function row( VF, context, overlay, entries, y, clef ) {
  const x = 40;
  const width = 800;
  const { notes } = drawStave( VF, context, {
    x, y, width, clef,
    notes: entries.map( ( [ key, accidental ] ) => ( {
      key,
      duration: 'w',
      accidental: accidental ?? undefined
    } ) ),
    formatWidth: width - 130
  } );

  // Harmonic number and cent deviation under each note. The x positions are
  // read back from the formatted notes rather than computed: VexFlow spaces
  // whole notes to fit the accidentals it had to insert, so an evenly divided
  // ruler drifts out of step with the noteheads by the end of the row.
  entries.forEach( ( [ , , harmonic, cents ], index ) => {
    const cx = notes[ index ].getAbsoluteX() + 6;
    overlay.text( String( harmonic ), cx, y + 152, {
      'font-weight': '700', 'text-anchor': 'middle', 'font-size': 15
    } );
    const label = cents === 0 ? '0' : `${ cents > 0 ? '+' : '\u2212' }${ Math.abs( cents ) }`;
    overlay.text( label, cx, y + 172, {
      'text-anchor': 'middle', 'font-size': 13,
      // The four partials that miss a key by more than a fifth of a semitone
      // are the ones worth looking at, so they are the ones in red.
      fill: Math.abs( cents ) >= 20 ? '#b33a3a' : '#555555'
    } );
  } );
}

export const definition = {
  id: 'harmonic-series-on-c2',
  output: 'harmonic-series-on-c2.svg',
  alt: 'The first sixteen harmonics of C2 on a bass and a treble stave, each labelled with '
       + 'its harmonic number and its deviation in cents from the nearest equal-tempered note. '
       + 'The seventh and fourteenth partials are 31 cents flat, the eleventh is 49 cents sharp, '
       + 'and the thirteenth is 41 cents sharp; the octaves and fifths are within a few cents.',
  width: 880,
  height: 490,
  render( { VF, context, overlay } ) {
    overlay.text( 'Harmonics 1\u20138', 40, 22, { 'font-weight': '700', 'font-size': 15 } );
    row( VF, context, overlay, LOWER, 34, 'bass' );
    overlay.text( 'Harmonics 9\u201316', 40, 248, { 'font-weight': '700', 'font-size': 15 } );
    row( VF, context, overlay, UPPER, 260, 'treble' );
    overlay.text( 'Under each note: the harmonic number, then how far that harmonic falls '
                  + 'from the nearest equal-tempered key, in cents.',
                  40, 468, { 'font-size': 13, fill: '#555555' } );
  }
};
