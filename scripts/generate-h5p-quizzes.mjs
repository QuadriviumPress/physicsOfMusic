#!/usr/bin/env node

import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve( path.dirname( fileURLToPath( import.meta.url ) ), '..' );
const CONTENT_ROOT = path.join( ROOT, 'h5p', 'content' );

const COMMON_BEHAVIOUR = {
  enableRetry: true,
  enableSolutionsButton: true,
  enableCheckButton: true
};

const A11Y = {
  a11yCheck: 'Check the answers. The responses will be marked as correct, incorrect, or unanswered.',
  a11yShowSolution: 'Show the solution. The task will be marked with its correct solution.',
  a11yRetry: 'Retry the task. Reset all responses and start the task over again.'
};

function uuid( seed ) {
  const bytes = crypto.createHash( 'sha256' ).update( seed ).digest().subarray( 0, 16 );
  bytes[ 6 ] = ( bytes[ 6 ] & 0x0f ) | 0x40;
  bytes[ 8 ] = ( bytes[ 8 ] & 0x3f ) | 0x80;
  const hex = bytes.toString( 'hex' );
  return `${hex.slice( 0, 8 )}-${hex.slice( 8, 12 )}-${hex.slice( 12, 16 )}-${hex.slice( 16, 20 )}-${hex.slice( 20 )}`;
}

function metadata( title, contentType ) {
  return { title, license: 'CC BY-NC-SA', licenseVersion: '4.0', contentType };
}

function feedback( correct ) {
  return {
    tip: '',
    chosenFeedback: correct ? 'Yes—this is one of the correct choices.' : 'Not this one. Revisit the chapter summary and try again.',
    notChosenFeedback: ''
  };
}

function multiChoice( seed, question, choices ) {
  const correctCount = choices.filter( choice => choice.correct ).length;
  return {
    library: 'H5P.MultiChoice 1.16',
    subContentId: uuid( `${seed}:multiple-choice` ),
    metadata: metadata( question, 'Multiple Choice' ),
    params: {
      question: `<p>${question}</p>`,
      answers: choices.map( choice => ( {
        text: `<div>${choice.text}</div>`,
        correct: choice.correct,
        tipsAndFeedback: feedback( choice.correct )
      } ) ),
      behaviour: {
        ...COMMON_BEHAVIOUR,
        singlePoint: correctCount === 1,
        randomAnswers: true,
        showSolutionsRequiresInput: true,
        autoCheck: false,
        passPercentage: 100,
        showScorePoints: true
      },
      overallFeedback: [ { from: 0, to: 100, feedback: 'You got @score of @total points.' } ],
      UI: {
        showSolutionButton: 'Show solution',
        tryAgainButton: 'Retry',
        checkAnswerButton: 'Check',
        submitAnswerButton: 'Submit',
        tipsLabel: 'Show tip',
        scoreBarLabel: 'You got :num out of :total points',
        tipAvailable: 'Tip available',
        feedbackAvailable: 'Feedback available',
        readFeedback: 'Read feedback',
        wrongAnswer: 'Wrong answer',
        correctAnswer: 'Correct answer',
        shouldCheck: 'Should have been checked',
        shouldNotCheck: 'Should not have been checked',
        noInput: 'Please answer before viewing the solution',
        ...A11Y
      }
    }
  };
}

function trueFalse( seed, question, correct, media ) {
  return {
    library: 'H5P.TrueFalse 1.8',
    subContentId: uuid( `${seed}:true-false` ),
    metadata: metadata( question, 'True/False Question' ),
    params: {
      question: `<p>${question}</p>`,
      correct: String( correct ),
      media: media ?? { disableImageZooming: false },
      behaviour: {
        ...COMMON_BEHAVIOUR,
        confirmCheckDialog: false,
        confirmRetryDialog: false,
        autoCheck: false
      },
      l10n: {
        trueText: 'True',
        falseText: 'False',
        score: 'You got @score of @total points',
        checkAnswer: 'Check',
        showSolutionButton: 'Show solution',
        tryAgain: 'Retry',
        submitAnswer: 'Submit',
        wrongAnswerMessage: 'That answer is incorrect.',
        correctAnswerMessage: 'Correct.',
        scoreBarLabel: 'You got :num out of :total points',
        ...A11Y
      }
    }
  };
}

function dragText( seed, taskDescription, textField, distractors = '' ) {
  return {
    library: 'H5P.DragText 1.10',
    subContentId: uuid( `${seed}:drag-text` ),
    metadata: metadata( taskDescription, 'Drag the Words' ),
    params: {
      taskDescription: `<p>${taskDescription}</p>`,
      textField,
      distractors,
      media: { disableImageZooming: false },
      behaviour: { ...COMMON_BEHAVIOUR, instantFeedback: false },
      overallFeedback: [ { from: 0, to: 100, feedback: 'You placed @score of @total terms correctly.' } ],
      checkAnswer: 'Check',
      submitAnswer: 'Submit',
      tryAgain: 'Retry',
      showSolution: 'Show solution',
      dropZoneIndex: 'Drop zone @index.',
      empty: 'Drop zone @index is empty.',
      contains: 'Drop zone @index contains draggable @draggable.',
      ariaDraggableIndex: '@index of @count draggables.',
      tipLabel: 'Show tip',
      correctText: 'Correct!',
      incorrectText: 'Incorrect!',
      resetDropTitle: 'Reset drop',
      resetDropDescription: 'Are you sure you want to reset this drop zone?',
      grabbed: 'Draggable is grabbed.',
      cancelledDragging: 'Cancelled dragging.',
      correctAnswer: 'Correct answer:',
      feedbackHeader: 'Feedback',
      scoreBarLabel: 'You got :num out of :total points',
      ...A11Y
    }
  };
}

function blanks( seed, prompt, lines ) {
  return {
    library: 'H5P.Blanks 1.14',
    subContentId: uuid( `${seed}:blanks` ),
    metadata: metadata( prompt, 'Fill in the Blanks' ),
    params: {
      text: `<p>${prompt}</p>`,
      questions: lines.map( line => `<p>${line}</p>` ),
      media: { disableImageZooming: false },
      behaviour: {
        ...COMMON_BEHAVIOUR,
        autoCheck: false,
        caseSensitive: false,
        showSolutionsRequiresInput: true,
        separateLines: false,
        confirmCheckDialog: false,
        confirmRetryDialog: false,
        acceptSpellingErrors: false
      },
      overallFeedback: [ { from: 0, to: 100, feedback: 'You completed @score of @total blanks correctly.' } ],
      showSolutions: 'Show solution',
      tryAgain: 'Retry',
      checkAnswer: 'Check',
      submitAnswer: 'Submit',
      notFilledOut: 'Please fill in all blanks to view the solution',
      answerIsCorrect: "':ans' is correct",
      answerIsWrong: "':ans' is wrong",
      answeredCorrectly: 'Answered correctly',
      answeredIncorrectly: 'Answered incorrectly',
      solutionLabel: 'Correct answer:',
      inputLabel: 'Blank input @num of @total',
      inputHasTipLabel: 'Tip available',
      tipLabel: 'Tip',
      scoreBarLabel: 'You got :num out of :total points',
      a11yCheckingModeHeader: 'Checking mode',
      ...A11Y
    }
  };
}

function markWords( seed, taskDescription, textField ) {
  return {
    library: 'H5P.MarkTheWords 1.11',
    subContentId: uuid( `${seed}:mark-words` ),
    metadata: metadata( taskDescription, 'Mark the Words' ),
    params: {
      taskDescription: `<p>${taskDescription}</p>`,
      textField,
      media: { disableImageZooming: false },
      behaviour: { ...COMMON_BEHAVIOUR, showScorePoints: true },
      overallFeedback: [ { from: 0, to: 100, feedback: 'You marked @score of @total terms correctly.' } ],
      checkAnswerButton: 'Check',
      submitAnswerButton: 'Submit',
      tryAgainButton: 'Retry',
      showSolutionButton: 'Show solution',
      correctAnswer: 'Correct!',
      incorrectAnswer: 'Incorrect!',
      missedAnswer: 'Answer not found!',
      displaySolutionDescription: 'The text now shows the solution.',
      scoreBarLabel: 'You got :num out of :total points',
      a11yFullTextLabel: 'Full readable text',
      a11yClickableTextLabel: 'Full text where words can be marked',
      a11ySolutionModeHeader: 'Solution mode',
      a11yCheckingHeader: 'Checking mode',
      ...A11Y
    }
  };
}

const imageMedia = {
  type: {
    library: 'H5P.Image 1.1',
    subContentId: uuid( 'ch12:chladni-image' ),
    metadata: metadata( 'Chladni figures', 'Image' ),
    params: {
      contentName: 'Image',
      alt: 'Four Chladni patterns formed by sand on vibrating square plates.',
      decorative: false,
      file: {
        path: 'images/ch12-chladni.png',
        mime: 'image/png',
        width: 1600,
        height: 512
      }
    }
  },
  disableImageZooming: false
};

const quizzes = [
  {
    chapter: 4,
    title: 'Resonance and Normal Modes Review',
    questions: [
      multiChoice( 'ch04', 'Which changes lower the resonance frequency of a Helmholtz resonator? Select both.', [
        { text: 'Increase the cavity volume.', correct: true },
        { text: 'Lengthen the effective neck.', correct: true },
        { text: 'Increase the neck area.', correct: false },
        { text: 'Increase the speed of sound.', correct: false }
      ] ),
      trueFalse( 'ch04', 'After transients die away, a driven oscillator vibrates at its natural frequency rather than at the driving frequency.', false ),
      dragText( 'ch04', 'Complete the linked descriptions of quality factor.', 'Quality factor is resonance frequency divided by *bandwidth*. A high-Q resonance has a *narrow* response peak and a *long* decay time.', '*wide*\n*short*' ),
      blanks( 'ch04', 'Complete the statement about degrees of freedom and modes.', [ 'A system with two degrees of freedom has *two/2* normal modes.' ] ),
      markWords( 'ch04', 'Mark the two things a resonator does to a source.', 'A resonator *transfers* energy efficiently to the air and *filters* the source spectrum; it does not create energy.' )
    ]
  },
  {
    chapter: 5,
    title: 'Fourier Analysis, Harmonics, and Timbre Review',
    questions: [
      multiChoice( 'ch05', 'Which statements describe a periodic musical waveform? Select all that apply.', [
        { text: 'Its sinusoidal components occur at whole-number multiples of the fundamental.', correct: true },
        { text: 'Its line spectrum has no energy between the harmonics.', correct: true },
        { text: 'Its harmonic phases uniquely determine its pitch.', correct: false },
        { text: 'It must contain only odd harmonics.', correct: false }
      ] ),
      trueFalse( 'ch05', 'For a steady complex tone, changing only the harmonic phases usually changes the perceived timbre dramatically.', false ),
      dragText( 'ch05', 'Match each feature to its spectral or time-frequency consequence.', 'A waveform discontinuity produces harmonics that fall roughly as *1/n*. A kink produces a faster *1/n²* falloff. A short analysis window improves *time* resolution; a long window improves *frequency* resolution.', '*1/n³*\n*phase*' ),
      blanks( 'ch05', 'Complete Fourier’s theorem for periodic sounds.', [ 'Any periodic waveform can be written as a sum of *sinusoids/sine waves* at whole-number multiples of one *fundamental* frequency.' ] ),
      markWords( 'ch05', 'Mark the four stages of an ADSR envelope.', '*Attack*, *decay*, *sustain*, and *release* describe how a note changes through time; spectral centroid and formants describe its spectrum.' )
    ]
  },
  {
    chapter: 6,
    title: 'The Ear and Hearing Review',
    questions: [
      multiChoice( 'ch06', 'Which choices reduce a musician’s risk from a loud rehearsal? Select all that apply.', [
        { text: 'Wear flat-response musician’s earplugs.', correct: true },
        { text: 'Take quiet breaks.', correct: true },
        { text: 'Increase distance from loud sources.', correct: true },
        { text: 'Rely on pain as an early warning.', correct: false }
      ] ),
      trueFalse( 'ch06', 'Inner hair cells provide most of the cochlear amplification, while outer hair cells send most auditory information to the brain.', false ),
      dragText( 'ch06', 'Place each cochlear role in the correct location or cell type.', 'The stiff, narrow *base* responds best to high frequencies; the floppy, wide *apex* responds best to low frequencies. *Inner hair cells* sense motion, while *outer hair cells* amplify and sharpen it.', '*pinna*\n*eardrum*' ),
      blanks( 'ch06', 'Complete the exposure-time rule.', [ 'For the same risk, every increase of *3/three* dB cuts the safe exposure time in *half/two*.' ] ),
      markWords( 'ch06', 'Mark the structures responsible for directional filtering, impedance matching, and frequency separation, in that order.', 'The *pinna* supplies direction-dependent filtering, the *middle ear* matches air to cochlear fluid, and the *basilar membrane* separates frequencies by place.' )
    ]
  },
  {
    chapter: 7,
    title: 'Loudness and Decibels Review',
    questions: [
      multiChoice( 'ch07', 'Eight identical, mutually incoherent sources play together. Approximately how much higher is their combined level than one source?', [
        { text: '9 dB', correct: true },
        { text: '3 dB', correct: false },
        { text: '8 dB', correct: false },
        { text: '18 dB', correct: false }
      ] ),
      trueFalse( 'ch07', 'Doubling sound-pressure amplitude increases sound-pressure level by about 6 dB.', true ),
      dragText( 'ch07', 'Complete these practical loudness and level rules.', '*40 phons* is defined as one sone. Each additional *10 phons* doubles loudness. Doubling outdoor distance changes level by *−6 dB*, while doubling incoherent sources changes it by *+3 dB*.', '*20 phons*\n*+6 dB*' ),
      blanks( 'ch07', 'Choose the correct logarithmic multiplier for each physical quantity.', [ 'Use *20* log₁₀ for pressure or amplitude ratios, but *10* log₁₀ for intensity or power ratios.' ] ),
      markWords( 'ch07', 'Mark the two ideas that explain why quiet playback loses bass.', 'At low levels the ear is less sensitive to *low frequencies*, and equal-loudness contours *flatten* as the overall level rises.' )
    ]
  },
  {
    chapter: 8,
    title: 'Pitch, Beats, Consonance, and Dissonance Review',
    questions: [
      multiChoice( 'ch08', 'Pure tones at 440 Hz and 446 Hz sound together. What beat rate is heard?', [
        { text: '6 beats per second', correct: true },
        { text: '3 beats per second', correct: false },
        { text: '443 beats per second', correct: false },
        { text: '886 beats per second', correct: false }
      ] ),
      trueFalse( 'ch08', 'A missing-fundamental pitch can be heard only when there is physical energy at the fundamental frequency.', false ),
      dragText( 'ch08', 'Match each auditory effect to its origin.', '*Beats* come from two nearby frequencies. *Roughness* occurs when partials share a critical band but beat too quickly to follow. A *combination tone* comes from nonlinearity, while a *missing fundamental* comes from harmonic pattern matching.', '*spectral centroid*\n*formant*' ),
      blanks( 'ch08', 'Infer the missing fundamental from the harmonic pattern.', [ 'Partials at 300, 400, and 500 Hz imply a missing fundamental of *100* Hz.' ] ),
      markWords( 'ch08', 'Mark the intervals where harmonic complex tones tend to produce strong roughness minima.', 'Strong minima occur near the *unison*, *octave*, *fifth*, and *fourth* because many partials coincide; a semitone usually remains rough.' )
    ]
  },
  {
    chapter: 9,
    title: 'Scales and Tuning Systems Review',
    questions: [
      multiChoice( 'ch09', 'Which statements are true of twelve-tone equal temperament? Select all that apply.', [
        { text: 'Every semitone has the ratio 2^(1/12).', correct: true },
        { text: 'The interval pattern is identical in every key.', correct: true },
        { text: 'Its fifth is about 2 cents narrow.', correct: true },
        { text: 'Its major thirds are exactly pure 5:4 ratios.', correct: false }
      ] ),
      trueFalse( 'ch09', 'A chain of twelve acoustically pure fifths closes exactly at seven octaves.', false ),
      dragText( 'ch09', 'Place each tuning-system description.', '*Pythagorean tuning* preserves pure fifths but has sharp thirds. *Just intonation* supplies pure home-key triads but resists modulation. *Quarter-comma meantone* makes pure thirds and one wolf. *Equal temperament* makes all keys equivalent.', '*stretched tuning*\n*free intonation*' ),
      blanks( 'ch09', 'Complete the cent divisions of the octave.', [ 'An octave contains *1200* cents, so an equal-tempered semitone contains *100* cents.' ] ),
      markWords( 'ch09', 'Mark the performers who can continuously bend pitch toward just intonation.', 'A *singer* and a *violinist* can adjust each note continuously; a pianist and an organist are constrained by fixed pitches.' )
    ]
  },
  {
    chapter: 10,
    title: 'String Instruments Review',
    questions: [
      multiChoice( 'ch10', 'With length and linear density fixed, by what factor must string tension change to raise the frequency by one octave?', [
        { text: 'Increase by a factor of 4.', correct: true },
        { text: 'Increase by a factor of 2.', correct: false },
        { text: 'Increase by a factor of √2.', correct: false },
        { text: 'Decrease by a factor of 4.', correct: false }
      ] ),
      trueFalse( 'ch10', 'An unplugged solid-body electric guitar is quiet and sustains well because it lacks an efficient soundboard coupling the strings to the air.', true ),
      dragText( 'ch10', 'Complete the cause-and-effect relationships for strings.', 'A *shorter length* raises frequency directly. *Greater tension* raises it by a square-root law. *Greater linear density* lowers it. *Winding* adds mass without the bending stiffness of a thick solid string.', '*longer length*\n*lighter winding*' ),
      blanks( 'ch10', 'Complete the pluck-position rule.', [ 'Plucking at one-fifth of a string’s length suppresses the *fifth/5th* harmonic and its *multiples*.' ] ),
      markWords( 'ch10', 'Mark the two components that chiefly couple an acoustic string to the air.', 'The string drives the *bridge*, which drives the *soundboard*; the large moving surface then radiates efficiently.' )
    ]
  },
  {
    chapter: 11,
    title: 'Wind Instruments and Air Columns Review',
    questions: [
      multiChoice( 'ch11', 'Compared with an open cylindrical pipe of the same length, what does a stopped cylindrical pipe do?', [
        { text: 'Sounds an octave lower and supports odd harmonics.', correct: true },
        { text: 'Sounds an octave higher and supports all harmonics.', correct: false },
        { text: 'Sounds at the same fundamental but lacks odd harmonics.', correct: false },
        { text: 'Has no standing-wave resonances.', correct: false }
      ] ),
      trueFalse( 'ch11', 'A cone closed at its apex has only odd harmonics, just like a stopped cylinder.', false ),
      dragText( 'ch11', 'Complete the boundary conditions for pressure and displacement.', 'At a closed end, air displacement has a *node* and pressure has an *antinode*. At an open end, displacement has an *antinode* and pressure has a *node*.', '*crest*\n*trough*' ),
      blanks( 'ch11', 'Complete the characteristic overblowing intervals.', [ 'A clarinet’s stopped-cylinder bore overblows to the *twelfth/12th*, while a conical saxophone overblows to the *octave/8ve*.' ] ),
      markWords( 'ch11', 'Mark the two brass-instrument features that pull resonances toward a useful harmonic series.', 'The *mouthpiece* lowers upper resonances and the *bell* raises lower resonances, aligning the playable series from the second resonance upward.' )
    ]
  },
  {
    chapter: 12,
    title: 'Percussion, Membranes, Bars, and Plates Review',
    questions: [
      multiChoice( 'ch12', 'Where should a free-free bar be supported to preserve its fundamental vibration?', [
        { text: 'At the fundamental’s nodes, about 22% from each end.', correct: true },
        { text: 'At its center antinode.', correct: false },
        { text: 'At both ends.', correct: false },
        { text: 'At any point; support position does not matter.', correct: false }
      ] ),
      trueFalse( 'ch12', 'In the Chladni patterns shown, sand collects along antinodes where the plate moves most.', false, imageMedia ),
      dragText( 'ch12', 'Match each vibrator to the beginning of its modal-frequency pattern.', 'An ideal string begins *1 : 2*. A free-free bar begins *1 : 2.76*. A circular membrane begins *1 : 1.59*. A timpano’s air-loaded sequence begins about *1 : 1.5*.', '*1 : 1.25*\n*1 : 3*' ),
      blanks( 'ch12', 'Complete the timpani pitch explanation.', [ 'The perceived timpani pitch is a *missing* fundamental one *octave* below its lowest prominent partial.' ] ),
      markWords( 'ch12', 'Mark the five named partials deliberately tuned in a church bell.', 'The five named partials are *hum*, *prime*, *tierce*, *quint*, and *nominal*; the traditional tierce is a minor third.' )
    ]
  },
  {
    chapter: 13,
    title: 'The Singing Voice Review',
    questions: [
      multiChoice( 'ch13', 'Why does the singer’s formant near 2.9 kHz improve projection? Select all that apply.', [
        { text: 'It falls in a relatively sparse region of the orchestra’s spectrum.', correct: true },
        { text: 'The ear is highly sensitive in that frequency region.', correct: true },
        { text: 'Low-frequency orchestral sound masks upward more readily than the voice cluster masks downward.', correct: true },
        { text: 'It moves every vocal harmonic down to the fundamental.', correct: false }
      ] ),
      trueFalse( 'ch13', 'In the source–filter model, the vocal folds can change pitch while the vocal tract largely preserves the vowel filter.', true ),
      dragText( 'ch13', 'Place each part of the voice model.', 'The *vocal folds* supply a harmonic source. The *vocal tract* supplies formant filtering. The first formant F1 tracks *jaw opening*, while F2 tracks *tongue position*.', '*ear canal*\n*chest cavity*' ),
      blanks( 'ch13', 'Complete the simple stopped-pipe model of the vocal tract.', [ 'A roughly *17* cm tract has formants near 500, *1500*, and 2500 Hz.' ] ),
      markWords( 'ch13', 'Mark the two distinct modes of vocal-fold vibration discussed as registers.', '*Chest voice* uses more of the fold depth, while *falsetto* uses mainly the edges; the passaggio is the transition between them.' )
    ]
  },
  {
    chapter: 14,
    title: 'Room Acoustics and Concert Halls Review',
    questions: [
      multiChoice( 'ch14', 'A diffuse room has volume 1000 m³ and total absorption 100 m² sabins. What reverberation time does the Sabine equation predict?', [
        { text: 'About 1.6 s', correct: true },
        { text: 'About 0.16 s', correct: false },
        { text: 'About 6.2 s', correct: false },
        { text: 'About 16 s', correct: false }
      ] ),
      trueFalse( 'ch14', 'Beyond the critical distance, level continues to fall by 6 dB for every doubling of distance because direct sound dominates.', false ),
      dragText( 'ch14', 'Match each part of a room response to its perceptual role.', '*Direct sound* locates the source. *Early reflections* add fused loudness and fullness. The *reverberant tail* conveys space. *Lateral energy* produces spaciousness through unequal signals at the ears.', '*ceiling energy*\n*floor absorption*' ),
      blanks( 'ch14', 'Complete the critical-distance statement.', [ 'Beyond the *critical* distance, the *reverberant* field dominates over direct sound.' ] ),
      markWords( 'ch14', 'Mark the three specular-reflection defects that diffusion helps cure.', 'Diffusion helps prevent distinct *echo*, repeated *flutter*, and curved-wall *focusing* by scattering reflections.' )
    ]
  },
  {
    chapter: 15,
    title: 'Electronic and Recorded Sound Review',
    questions: [
      multiChoice( 'ch15', 'Where must an anti-aliasing low-pass filter act?', [
        { text: 'Before sampling, while frequencies above Nyquist can still be removed.', correct: true },
        { text: 'After sampling, once aliases are visible.', correct: false },
        { text: 'Only during playback.', correct: false },
        { text: 'Only before analog amplification.', correct: false }
      ] ),
      trueFalse( 'ch15', 'Dither improves low-level digital sound by reducing the total error energy introduced during quantization.', false ),
      dragText( 'ch15', 'Match each transducer or polar pattern to its operating principle.', 'A *dynamic microphone* uses a coil and magnet. A *condenser microphone* uses a variable capacitor. An *omnidirectional* capsule senses pressure, while a *figure-of-eight* capsule senses pressure difference.', '*magnetic pickup*\n*cardioid*' ),
      blanks( 'ch15', 'Estimate ideal quantization dynamic range.', [ 'At roughly 6 dB per bit, ideal 16-bit audio provides about *96* dB of dynamic range.' ] ),
      markWords( 'ch15', 'Mark the two processes in this sentence that create frequency components not present in the input.', '*FM synthesis* generates sidebands, and *nonlinear distortion* creates new frequencies; subtractive filtering only rebalances frequencies already present.' )
    ]
  }
];

const dependencies = [
  [ 'H5P.QuestionSet', 1, 21 ],
  [ 'H5P.MultiChoice', 1, 16 ],
  [ 'H5P.TrueFalse', 1, 8 ],
  [ 'H5P.DragText', 1, 10 ],
  [ 'H5P.Blanks', 1, 14 ],
  [ 'H5P.MarkTheWords', 1, 11 ]
];

function dependency( [ machineName, majorVersion, minorVersion ] ) {
  return { machineName, majorVersion, minorVersion };
}

function questionSet( quiz ) {
  return {
    progressType: 'dots',
    passPercentage: 80,
    questions: quiz.questions,
    introPage: {
      showIntroPage: false,
      title: quiz.title,
      introduction: '<p>Five short questions review the chapter.</p>',
      startButtonText: 'Start review'
    },
    texts: {
      prevButton: 'Previous question',
      previous: 'Previous',
      nextButton: 'Next question',
      next: 'Next',
      finishButton: 'Finish',
      submitButton: 'Submit',
      textualProgress: 'Question @current of @total',
      jumpToQuestion: 'Question %d of %total',
      questionLabel: 'Question',
      readSpeakerProgress: 'Question @current of @total',
      unansweredText: 'Unanswered',
      answeredText: 'Answered',
      currentQuestionText: 'Current question',
      navigationLabel: 'Questions',
      questionSetInstruction: 'Choose a question to display'
    },
    disableBackwardsNavigation: false,
    randomQuestions: false,
    endGame: {
      showResultPage: true,
      showSolutionButton: true,
      showRetryButton: true,
      noResultMessage: 'Finished',
      message: 'Chapter review complete',
      amountCorrect: '@finals of @totals correct',
      scoreBarLabel: 'You got @finals out of @totals points',
      scoreHeader: 'Score',
      overallFeedback: [ { from: 0, to: 100, feedback: 'You earned @score of @total points.' } ],
      solutionButtonText: 'Show solutions',
      retryButtonText: 'Retry',
      finishButtonText: 'Finish',
      submitButtonText: 'Submit',
      showAnimations: false,
      skippable: false,
      skipButtonText: 'Skip video'
    },
    override: {
      checkButton: true,
      showSolutionButton: 'on',
      retryButton: 'on'
    }
  };
}

for ( const quiz of quizzes ) {
  const chapter = String( quiz.chapter ).padStart( 2, '0' );
  const id = `ch${chapter}-chapter-review`;
  const root = path.join( CONTENT_ROOT, id );
  const content = path.join( root, 'content' );
  fs.mkdirSync( content, { recursive: true } );

  const preloadedDependencies = dependencies.map( dependency );
  if ( quiz.chapter === 12 ) preloadedDependencies.push( dependency( [ 'H5P.Image', 1, 1 ] ) );

  const manifest = {
    title: quiz.title,
    language: 'en',
    mainLibrary: 'H5P.QuestionSet',
    embedTypes: [ 'iframe' ],
    license: 'CC BY-NC-SA',
    licenseVersion: '4.0',
    preloadedDependencies
  };

  fs.writeFileSync( path.join( root, 'h5p.json' ), `${JSON.stringify( manifest, null, 2 )}\n` );
  fs.writeFileSync( path.join( content, 'content.json' ), `${JSON.stringify( questionSet( quiz ), null, 2 )}\n` );

  if ( quiz.chapter === 12 ) {
    const imageDirectory = path.join( content, 'images' );
    fs.mkdirSync( imageDirectory, { recursive: true } );
    fs.copyFileSync( path.join( ROOT, 'images', 'ch12-chladni.png' ), path.join( imageDirectory, 'ch12-chladni.png' ) );
  }
}

console.log( `Generated ${quizzes.length} H5P chapter reviews (${quizzes.reduce( ( total, quiz ) => total + quiz.questions.length, 0 )} questions).` );
