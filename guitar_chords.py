import itertools

# list of available notes in western music 

# at first lets determine available notes 

# lets start from A, it does not really matter which note are first 

chromatic_scale_flats = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
chromatic_scale_sharps = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

# a recipie with steps for creating major scale 
major_scale_steps = [2, 2, 1, 2, 2, 2, 1]

def generate_chromatic_scale(root_note ):
    # TODO handle errors 
    return  chromatic_scale_flats[chromatic_scale_flats.index(root_note) : ] + chromatic_scale_flats[: chromatic_scale_flats.index(root_note)]

# Generating scale is based on the chromatic scale. User passes recipe which is the list of steps (1 -half step, 2-whole step) from notes starting from root_note 
def generate_scale(root_note, recipe):
    scale = [] 
    index = 0
    # generate chromatic scale - on top of this the major scale will be generated 
    chromatic_scale_flats = generate_chromatic_scale(root_note)

    # Add root note to the major scale list 
    scale.append(chromatic_scale_flats[0])

    # Iterate over chromatic scale list with given recipe 
    for i in range(0, len(recipe) - 1): 
        index = index + recipe[i] 
        scale.append(chromatic_scale_flats[index])

    return scale 

def generate_major_scale(root_note):
    scale_steps = [2, 2, 1, 2, 2, 2, 1]
    return generate_scale(root_note, scale_steps) 

def generate_minor_scale(root_note):
    pass

# return number of semitones between first_note and second_note 
def calculate_interval_between_notes(first_note, second_note):
    chromatic_scale = generate_chromatic_scale(first_note)
    return chromatic_scale.index(second_note)

def get_chord_type(chord_notes):

    interval = calculate_interval_between_notes(chord_notes[0], chord_notes[1])
    if(interval == 3):
        return "{} minor chord".format(chord_notes[0])
    elif(interval == 4):
        return "{} major chord".format(chord_notes[0])
    else:
        return "other chord "
    


#TODO obsluga bledow 
def get_basic_chord_from_major_scale(scale_root_note, chord_degree, chord_note_count):
    #generate major scale based on given root note 
    chord_notes = []

    #create circular iterator 
    major_scale_pool = itertools.cycle(generate_major_scale(scale_root_note))

    #get to the root note of the chord 
    for i in range(0, chord_degree - 1 ):
        next(major_scale_pool)

    # Start building chord 
    # When building chords on scales we ommiting every second note (in basic chords) 
    for i in range(0, chord_note_count):
        chord_notes.append(next(major_scale_pool))
        next(major_scale_pool)

    return chord_notes 

if __name__ == "__main__":


    C_major_scale = generate_scale('C', major_scale_steps)
    print(C_major_scale)

    chord = get_basic_chord_from_major_scale('C', 7, 3) # TODO Bug with G major chord 


    print(get_chord_type(chord))