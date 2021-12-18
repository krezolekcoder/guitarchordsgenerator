import unittest
from chords_generator import ChordsGenerator, major_scale_steps, MyException

class TestChordsGenerator(unittest.TestCase):

    def test_majorscalegen(self):
        chords_gen = ChordsGenerator()

        c_major_scale = chords_gen.generate_major_scale('C')

        self.assertEqual(c_major_scale, ['C', 'D', 'E', 'F', 'G', 'A', 'B'])

        with self.assertRaises(MyException) as context:
            chords_gen.generate_major_scale('H')
        self.assertTrue('Root note not recognized' in str(context.exception))

    
    def test_major_chords_gen(self):
        chords_gen = ChordsGenerator()

        c_maj_chord = chords_gen.generate_chord('C', 'Major')

        self.assertEqual(c_maj_chord, ['C', 'E', 'G'])

        d_maj_chord = chords_gen.generate_chord('D', 'Major')

        self.assertEqual(d_maj_chord, ['D', 'F#', 'A'])

        a_sharp_maj_chord = chords_gen.generate_chord('A#', 'Major')

        self.assertEqual(a_sharp_maj_chord, ['A#', 'D', 'F'])

        chord_type = chords_gen.get_chord_type(a_sharp_maj_chord)

        self.assertEqual(chord_type, 'A# Major')

        with self.assertRaises(MyException) as context:
            chords_gen.generate_chord('H', 'Major')
        self.assertTrue('Root note not recognized' in str(context.exception))

        with self.assertRaises(MyException) as context:
            chords_gen.generate_chord('H', 'Elooo')
        self.assertTrue('Unknown chord type' in str(context.exception))

    def test_minor_chords_gen(self):
        chords_gen = ChordsGenerator()

        c_min_chord = chords_gen.generate_chord('C', 'Minor')
        
        self.assertEqual(c_min_chord, ['C', 'D#', 'G'])

        d_min_chord = chords_gen.generate_chord('D', 'Minor')

        self.assertEqual(d_min_chord, ['D', 'F', 'A'])

        chord_type = chords_gen.get_chord_type(d_min_chord)

        self.assertEqual(chord_type, 'D Minor')

        g_sharp_minor_chord = chords_gen.generate_chord('G#', 'Minor')

        self.assertEqual(g_sharp_minor_chord, ['G#', 'B', 'D#'])


if __name__ == '__main__':
    unittest.main()