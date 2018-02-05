import random
import colors as col

printInfo = False

def generate(timeBeats, timeQuarter):
    global sequences, seq0, seq1, seq2, impBeats, printInfo

    if printInfo:
        print("\ngen\tGenerating beat:", timeBeats, "/", timeQuarter)

    # Clear the lists on each (re)generation
    seq0 = []
    seq1 = []
    seq2 = []

    # Find the beats required for establishing the measure feel
    # I called these impBeats, short for importantBeats
    # Will return a list consiting of 2, 3 or 4's
    # They represent the time relative to the previous trigger:
    # [2, 3, 2] = [0, 2, 5] or [1, 0, 1, 0, 0, 1, 0]
    findImportantBeats(timeBeats)

    # Shuffled for more variation
    random.shuffle(impBeats)

    if printInfo:
        print(col.info + "\n_\tDivided measure into prioritized hits:", impBeats + col.reset)

    # Assing the impBeats to the kick or the snare
    assignImportant(timeBeats)

    # Fill shit up with hats yo
    fillHats(timeBeats)

    # Put all sequences into a list which will be read by the playback class
    sequences = [seq0, seq1, seq2]

def assignImportant(timeBeats):
    global printInfo, impBeatsAbs

    if printInfo:
        print("_\tAssigning beats..")

    # Fill each list with the right amount of non-triggers
    for i in range(timeBeats):
        seq0.append(0)
        seq1.append(0)
        seq2.append(0)

    # Put a kick at 0
    seq0[0] = 1

    # Convert beat values from relative to absolute
    # [2, 3, 2] = [0, 2, 5]
    impBeatsAbs = relToAbs(impBeats)
    # print(impBeats, impBeatsAbs)

    # For each importantBeat
    # Assign it to kick or snare
    for i in range(len(impBeatsAbs)):
        x = random.randint(0, 9)

        # random = 0 / 1 / 2 / 3
        # Beat will be assigned to kick
        if x <= 3:
            seq0[impBeatsAbs[i]] = 1

        # random = 4 / 5 / 6 / 7
        # Beat will be assigned to snare
        elif x <= 7:
            seq1[impBeatsAbs[i]] = 1

        # random = 8 / 9
        # Beat will be assigned to both kick and snare
        else:
            seq0[impBeatsAbs[i]] = 1
            seq1[impBeatsAbs[i]] = 1

    # Remove snares at 0
    seq1[0] = 0

    # Check if there are any snares at all
    if seq1.count(1) < 1:
        # Insert a snare trigger at the last important beat
        seq1[impBeatsAbs[-1]] = 1

    for i in range(len(seq0)):
        # Randomly adds a 2 kick after: 0 1
        if seq0[i-1] != 0 and seq0[i-2] == 0 and random.choice([True, False]):
            seq0[i] = 2

    if printInfo:
        print(col.info + "Kick  ", seq0, "\nSnare ", seq1, "\nHihats", seq2, "\n" + reset)

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
        print(col.error + "Error. Something went wrong with findImportantBeats(), timeBeats might be out of range" + col.reset)

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

def fillHats(timeBeats):
    global seq0, seq1, seq2

    # Append a 0 to prevent index out of bounds
    seq0.append(0)
    seq2.append(0)

    for i in range(timeBeats):
        # Randomly add a hihat or kick after each trigger without kick or snare
        if seq0[i] == 0 and seq1[i] == 0 and random.choice([True, False]):
            seq2[i+1] = 1

        # Add a hihat after each trigger with a snare
        elif seq1[i] == 1:
            seq2[i+1] = 1

        else:
            # Index wraps around when negative
            # Thanks Python!
            seq2[i] = 2

    # Remove last item
    seq0.pop()
    seq2.pop()

    # Put a hihat at 0
    seq2[0] = 1
