import { drawStave } from '../figure-helpers.mjs';

/**
 * A C major scale written once, with each degree's tuning in three systems
 * given beneath it in cents from equal temperament.
 *
 * The staff is doing something a table cannot: it puts the numbers under the
 * notes a reader already knows, so the argument of Chapter 9 -- that these are
 * all the same seven notes, differing by a few hundredths of a semitone -- is
 * visible rather than asserted.
 */

const CENTS = value => 1200 * Math.log2( value );

// Just ratios for the major scale, and the Pythagorean chain-of-fifths values.
const DEGREES = [
  { key: 'c/4', name: 'C', just: 1, pyth: 1 },
  { key: 'd/4', name: 'D', just: 9 / 8, pyth: 9 / 8 },
  { key: 'e/4', name: 'E', just: 5 / 4, pyth: 81 / 64 },
  { key: 'f/4', name: 'F', just: 4 / 3, pyth: 4 / 3 },
  { key: 'g/4', name: 'G', just: 3 / 2, pyth: 3 / 2 },
  { key: 'a/4', name: 'A', just: 5 / 3, pyth: 27 / 16 },
  { key: 'b/4', name: 'B', just: 15 / 8, pyth: 243 / 128 },
  { key: 'c/5', name: 'C', just: 2, pyth: 2 }
];

/**
 * Formats a cent deviation with an explicit sign and a true minus sign.
 *
 * @param {number} value - Deviation in cents.
 * @returns {string}
 */
function signed( value ) {
  const rounded = Math.round( value );
  if ( rounded === 0 ) return '0';
  return `${ rounded > 0 ? '+' : '−' }${ Math.abs( rounded ) }`;
}

export const definition = {
  id: 'tuning-comparison',
  output: 'tuning-comparison.svg',
  alt: 'A C major scale on a treble stave. Under each note are three numbers giving its '
       + 'deviation in cents from equal temperament in just intonation, in Pythagorean '
       + 'tuning, and in equal temperament itself. Just intonation puts E 14 cents flat '
       + 'and A 16 cents flat; Pythagorean puts E 8 cents sharp and B 10 cents sharp; '
       + 'equal temperament is zero throughout by definition.',
  width: 880,
  height: 330,
  render( { VF, context, overlay } ) {
    const x = 150;
    const width = 680;
    const { notes } = drawStave( VF, context, {
      x, y: 30, width, clef: 'treble',
      notes: DEGREES.map( degree => ( { key: degree.key, duration: 'w' } ) ),
      formatWidth: width - 120
    } );

    // Equal-tempered cents for each scale degree, in order.
    const equal = [ 0, 200, 400, 500, 700, 900, 1100, 1200 ];

    const y0 = 172;
    [ 'just', 'Pythagorean', 'equal' ].forEach( ( label, row ) => {
      const colour = [ '#2e7d5b', '#1769aa', '#555555' ][ row ];
      overlay.text( label, x - 8, y0 + row * 30, {
        'text-anchor': 'end', 'font-size': 14, 'font-weight': '700', fill: colour
      } );
      DEGREES.forEach( ( degree, index ) => {
        const value = label === 'just' ? CENTS( degree.just ) - equal[ index ]
                    : label === 'Pythagorean' ? CENTS( degree.pyth ) - equal[ index ]
                    : 0;
        const cx = notes[ index ].getAbsoluteX() + 6;
        overlay.text( signed( value ), cx, y0 + row * 30, {
          'text-anchor': 'middle', 'font-size': 14,
          'font-weight': Math.abs( value ) >= 10 ? '700' : '400',
          fill: Math.abs( value ) >= 10 ? '#b33a3a' : colour
        } );
        if ( row === 0 ) {
          overlay.text( degree.name, cx, 148, {
            'text-anchor': 'middle', 'font-size': 15, 'font-weight': '700'
          } );
        }
      } );
    } );

    overlay.text( 'cents from equal temperament; red where the departure exceeds 10 cents',
                  x - 8, y0 + 3 * 30 + 6, { 'font-size': 13, fill: '#555555' } );
  }
};
