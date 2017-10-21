def generate(generation, timeBeats, timeMeasure):
    global sequences, seq0, seq1, seq2

    if generation:
        print("\nGenerating beat:", timeBeats, "/", timeMeasure)
    else:
        # Sequence of drumtriggers
        # 0 no trigger
        # 1 normal trigger, plays a sound
        # 2 random trigger, sometimes plays a sound
        seq0 = [1, 0, 1, 0, 1, 0, 1, 0]
        seq1 = [0, 0, 1, 0, 0, 0, 1, 0]
        seq2 = [2, 1, 0, 2, 0, 1, 2, 1]

    sequences = [seq0, seq1, seq2]
    print("\nBeat generated\n")
