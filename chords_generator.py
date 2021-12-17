import itertools
# list of available notes in western music 

# at first lets determine available notes 

# lets start from A, it does not really matter which note are first 

chromatic_scale_flats = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
chromatic_scale_sharps = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
chord_types = ['Major' , 'Minor', 'Maj7']
# a recipie with steps for creating major scale 
major_scale_steps = [2, 2, 1, 2, 2, 2]

class MyException(Exception):
    pass

class ChordsGenerator:
    def __generate_chromatic_scale(self, root_note):
        
        chromatic_scale = []
        if root_note in chromatic_scale_flats and root_note in chromatic_scale_sharps:
            chromatic_scale = chromatic_scale_flats[chromatic_scale_flats.index(root_note) : ] + chromatic_scale_flats[: chromatic_scale_flats.index(root_note)]
        elif root_note in chromatic_scale_sharps:
            chromatic_scale = chromatic_scale_sharps[chromatic_scale_sharps.index(root_note) : ] + chromatic_scale_sharps[: chromatic_scale_sharps.index(root_note)]
        elif root_note in chromatic_scale_flats:
            chromatic_scale = chromatic_scale_sharps[chromatic_scale_flats.index(root_note) : ] + chromatic_scale_flats[: chromatic_scale_flats.index(root_note)]
        else :
            raise(MyException(' Root note not recognized'))
        return chromatic_scale 

    def __calculate_interval_between_notes(self, first_note, second_note):
        chromatic_scale = self.__generate_chromatic_scale(first_note)
        return chromatic_scale.index(second_note)

    def generate_scale(self, root_note, recipe):
        scale = [] 
        index = 0
        # generate chromatic scale - on top of this the major scale will be generated 
        chromatic_scale = self.__generate_chromatic_scale(root_note)

        # Generate list of indexes of given recipe from chromatic scale
        scale_absolute = []
        current_absolute_val = 0
        for step in recipe:
            current_absolute_val += step
            scale_absolute.append(current_absolute_val)
        # Add root note to the major scale list 
        scale.append(chromatic_scale[0])
        
        # Get notes from  given index of chromatic scale 
        for absolute_val in scale_absolute:
            scale.append(chromatic_scale[absolute_val])

        return scale 
    
    def generate_major_scale(self, root_note):
        return self.generate_scale(root_note, major_scale_steps) 

    def get_chord_type(self,chord_notes):

        interval = self.__calculate_interval_between_notes(chord_notes[0], chord_notes[1])
        if(interval == 3):
            return "{} minor chord".format(chord_notes[0])
        elif(interval == 4):
            return "{} major chord".format(chord_notes[0])
        else:
            return "other chord " 

    def get_basic_chord_from_major_scale(self, mjr_scale_root_note, chord_degree, chord_notes_count):
            #generate major scale based on given root note 
        chord_notes = []

        #create circular iterator 
        major_scale_iterable = itertools.cycle(self.generate_major_scale(mjr_scale_root_note))

        #get to the root note of the chord 
        for i in range(0, chord_degree - 1 ):
            next(major_scale_iterable)

        # When building chords on scales we ommiting every second note of the scale 
        # f.ex C major scale C D E F G A B C. C major chord - C E G , D minor - D F A 
            chord_notes.append(next(major_scale_iterable))
            next(major_scale_iterable)

        return chord_notes

    def generate_chord(self, chord_root_note, chord_type):
        
        if chord_type not in chord_types:
            raise(MyException('Unknown chord type '))

        generated_chord = [] 
        if chord_type == 'Major':
        # in order to generate major chord we first need to generate the major scale of the root note of that chord 
            generated_chord = self.get_basic_chord_from_major_scale(chord_root_note, 1, 3)

        elif chord_type == 'Minor':
        #in order to generate minor chord we first need to generate the major scale of the note that is 2 semitones back 
        # and then get the second chord of that major scale which is minor  
            chromatic_scale = self.__generate_chromatic_scale(chord_root_note)

            major_scale_index = chromatic_scale.index(-2)

            generated_chord = self.get_basic_chord_from_major_scale(chromatic_scale[major_scale_index], 2, 3)

        return generated_chord


if __name__ == "__main__":

    chord = ChordsGenerator()

    print(chord.generate_chord('C', 'Major'))

