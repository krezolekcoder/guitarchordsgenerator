

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



# TODO implement this 

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
        print(index)
        scale.append(chromatic_scale_flats[index])

    return scale 

def generate_major_scale(root_note):
    scale_steps = [2, 2, 1, 2, 2, 2, 1]
    return generate_scale(root_note, scale_steps) 

def generate_minor_scale(root_note):
    pass

# Function returns the degree note of major scale determined by root note 

def get_major_scale_degree(root_note, degree_number):
    pass

def calculate_interval_between_notes(first_note, second_note):
    pass
if __name__ == "__main__":


    C_major_scale = generate_scale('C', major_scale_steps)
    print(C_major_scale)


