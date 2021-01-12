

# list of available notes in western music 

# at first lets determine available notes 

# lets start from A, it does not really matter which note are first 

chromatic_scale_flats = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
chromatic_scale_sharps = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

# a recipie with steps for creating major scale 


def generate_notes_in_string(pitch_note ):
    # TODO handle errors 
    return  chromatic_scale_flats[chromatic_scale_flats.index(pitch_note) : ] + chromatic_scale_flats[: chromatic_scale_flats.index(pitch_note)]

def generate_scale()

if __name__ == "__main__":

    # print(generate_notes_in_string('E'))
    E_string = generate_notes_in_string('E')
    B_string = generate_notes_in_string('B')
    G_string = generate_notes_in_string('G')
    D_string = generate_notes_in_string('D')
    A_string = generate_notes_in_string('A')
    E6_string = generate_notes_in_string('E')

    print(E_string)
    print(B_string) 
    print(G_string)
    print(D_string) 
    print(A_string)
    print(E6_string) 


