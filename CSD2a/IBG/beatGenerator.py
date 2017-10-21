import random

def generate(generation, timeBeats, timeQuarter):
    global sequences, seq0, seq1, seq2, importantBeats

    if generation:
        # print("\ngen\tGenerating beat:", timeBeats, "/", timeQuarter)
        findImportantBeats(timeBeats)
        print("gen\tDivided measure into prioritized hits:", importantBeats)

        seq0 = [1, 0, 1, 0, 1, 0, 1, 0]
        seq1 = [0, 0, 1, 0, 0, 0, 1, 0]
        seq2 = [2, 1, 0, 2, 0, 1, 2, 1]
    else:
        # Play the preset beat (boooring)
        seq0 = [1, 0, 1, 0, 1, 0, 1, 0]
        seq1 = [0, 0, 1, 0, 0, 0, 1, 0]
        seq2 = [2, 1, 0, 2, 0, 1, 2, 1]

    # Put all sequences into a list which will be read by the playback class
    sequences = [seq0, seq1, seq2]

def findImportantBeats(timeBeats):
    global importantBeats

    if timeBeats == 4:
        importantBeats = [2,2]
    elif timeBeats == 5:
        importantBeats = [3,2]
    elif timeBeats == 6:
        options = [[3,3], [2,2,2]]
        importantBeats = options[random.randint(0,1)]
    elif timeBeats == 7:
        options = [[3,2,2], [2,2,2]]
        importantBeats = options[random.randint(0,1)]
    elif timeBeats == 8:
        options = [[3,3,2], [4,4]]
        importantBeats = options[random.randint(0,1)]
    elif timeBeats == 9:
        options = [[3,3,3], [2,2,2,3]]
        importantBeats = options[random.randint(0,1)]
    elif timeBeats == 10:
        options = [[3,3,2,2], [4,4,2]]
        importantBeats = options[random.randint(0,1)]
    elif timeBeats == 11:
        options = [[3,3,3,2], [4,4,3]]
        importantBeats = options[random.randint(0,1)]
    elif timeBeats == 12:
        options = [[3,3,3,3], [4,4,4]]
        importantBeats = options[random.randint(0,1)]
    else:
        print("Dit zou niet moeten kunnen.")

# Sequence of drumtriggers
# 0 no trigger
# 1 normal trigger, plays a sound
# 2 random trigger, sometimes plays a sound
