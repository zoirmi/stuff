import random
from copy import deepcopy
from music21 import *


def create_etude(num_repeats):
    etude = stream.Stream()

    # Notes for pattern A
    A_note1 = note.Note('A1')
    A_note1.duration.type = 'quarter'
    A_note2 = note.Note('A1')
    A_note2.duration.type = 'quarter'

    # Notes for pattern B
    B_note1 = note.Note('A1')
    B_note1.duration.type = 'quarter'
    B_note2 = note.Note('A1')
    B_note2.duration.type = 'eighth'
    B_note3 = note.Note('A1')
    B_note3.duration.type = 'eighth'

    # Notes for pattern C
    C_note1 = note.Note('A1')
    C_note1.duration.type = 'eighth'
    C_note2 = note.Note('A1')
    C_note2.duration.type = 'eighth'
    C_note3 = note.Note('A1')
    C_note3.duration.type = 'quarter'

    # Notes for pattern D
    D_note1 = note.Note('A1')
    D_note1.duration.type = 'quarter'
    D_note1.duration.dots = 1
    D_note2 = note.Note('A1')
    D_note2.duration.type = 'eighth'

    # Half bar patterns
    pattern_A = stream.Stream()
    pattern_B = stream.Stream()
    pattern_C = stream.Stream()
    pattern_D = stream.Stream()

    pattern_A.append([A_note1, A_note2])
    pattern_B.append([B_note1, B_note2, B_note3])
    pattern_C.append([C_note1, C_note2, C_note3])
    pattern_D.append([D_note1, D_note2])

    patterns = [pattern_A, pattern_B, pattern_C, pattern_D]
    
    for i in range(num_repeats):
       pattern = random.choice(patterns)
       etude.append(deepcopy(pattern)) 

    return etude

etude = create_etude(num_repeats=160)  

for measure in etude.recurse().getElementsByClass('Measure'):
    measure.clef = None
etude.show()

