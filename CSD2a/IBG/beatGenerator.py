import random



def generate(generation, timeBeats, timeQuarter):
    global sequences, seq0, seq1, seq2, impBeats
    # print("\ngen\tGenerating beat:", timeBeats, "/", timeQuarter)

    # Clear the lists on each (re)generation
    seq0 = []
    seq1 = []
    seq2 = []

    if generation:
        # Find the beats required for establishing the measure feel
        # I called these impBeats, short for importantBeats
        # Will return a list consiting of 2, 3 or 4's
        # They represent the time relative to the previous trigger:
        # [2, 3, 2] = [0, 2, 5] or [1, 0, 1, 0, 0, 1, 0]
        findImportantBeats(timeBeats)

        # Shuffled for more variation
        random.shuffle(impBeats)
        print("\n_\tDivided measure into prioritized hits:", impBeats)

        # Assing the impBeats to the kick or the snare
        assignImportant(timeBeats)

    else:
        # Play the preset beat (boooring)
        seq0 = [1, 0, 1, 0]
        seq1 = [0, 0, 1, 0]
        seq2 = [2, 1, 0, 2]

    # Put all sequences into a list which will be read by the playback class
    sequences = [seq0, seq1, seq2]

def assignImportant(timeBeats):
    print("_\tAssigning beats..")

    # Fill each list with the right amount of non-triggers
    for i in range(timeBeats):
        seq0.append(0)
        seq1.append(0)
        seq2.append(0)

    # Put a kick at 0 because reasons
    seq0[0] = 1

    # Convert beat values from relative to absolute
    # [2, 3, 2] = [0, 2, 5]
    impBeatsAbs = relToAbs(impBeats)
    # print(impBeats, impBeatsAbs)

    # Assign the beats to kick or snare
    for i in range(len(impBeatsAbs)):
        x = random.randint(0, 2)
        if x == 0:
            # Beat will be assigned to kick
            seq0[impBeatsAbs[i]] = 1
        elif x == 1:
            # Beat will be assigned to snare
            seq1[impBeatsAbs[i]] = 1
        else:
            # Beat will be assigned to both
            seq0[impBeatsAbs[i]] = 1
            seq1[impBeatsAbs[i]] = 1

    # Print the results
    print("Kick  ", seq0, "\nSnare ", seq1, "\nHihats", seq2, "\n")

def findImportantBeats(timeBeats):
    global impBeats

    if timeBeats == 4:
        impBeats = [2,2]
    elif timeBeats == 5:
        impBeats = [3,2]
    elif timeBeats == 6:
        options = [[3,3], [2,2,2]]
        impBeats = options[random.randint(0,1)]
    elif timeBeats == 7:
        options = [[3,2,2], [3,3,1]]
        impBeats = options[random.randint(0,1)]
    elif timeBeats == 8:
        options = [[3,3,2], [4,4], [4,2,2]]
        impBeats = options[random.randint(0,2)]
    elif timeBeats == 9:
        options = [[3,3,3], [3,2,2,2], [4,3,2]]
        impBeats = options[random.randint(0,2)]
    elif timeBeats == 10:
        options = [[3,3,2,2], [4,4,2], [4,3,2]]
        impBeats = options[random.randint(0,2)]
    elif timeBeats == 11:
        options = [[3,3,3,2], [3,2,2,2,2], [4,3,2,2]]
        impBeats = options[random.randint(0,2)]
    elif timeBeats == 12:
        options = [[3,3,3,3], [4,4,4], [4,3,3,2]]
        impBeats = options[random.randint(0,2)]
    else:
        print("Error. Something went wrong with findImportantBeats(), timeBeats might be out of range")

def relToAbs(listIn):
    listIn.insert(0, 0)
    listOut = []
    y = 0
    for i in range(len(listIn)):
        y += listIn[i]
        listOut.append(y)
    listIn.pop(0)
    listOut.pop()
    return listOut

# Sequence of drumtriggers
# 0 no trigger
# 1 normal trigger, plays a sound
# 2 random trigger, sometimes plays a sound
