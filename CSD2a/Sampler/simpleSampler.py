# TODO
# - Option to input each list at booting the program
# - Add variation over time: list manipulation
#       if interval has passed else wait a ~10ms
# - check all files ending with *.wav -> laad deze

# ISSUES
# - Glitches when BPM < 120
# - Samples are cutoff when a new sample is triggered (clicky)
# - Beat sometimes lags a bit

import simpleaudio as sa
import time
import random

# Class which plays a single sample
class samplePlayer:
    def __init__(self, sample=0):
        self.sampleIndex = sample
        
    def playSample(self, trig):
        global samples
        self.trig = trig
        
        if trig == 1:
            # Normal trigger
            playObj = samples[self.sampleIndex].play()
            
        elif trig == 2:
            if random.randint(0, 1) == 1:
                # Random trigger (doesn't always trigger)
                playObj = samples[self.sampleIndex].play()

print("\n / / / / simpleSampler / / / / \n ")

# Drumkit selection
validKit = False
print("1: Tape \n2: 808 \n3: 909 \n4: DMX")
inputKit = input("Choose a drumkit: ")

# Check if drumkit input is valid and try again if needed
while validKit == False:
    if inputKit.isdigit() and int(inputKit) < 5:
        # Set Kit, exit loop
        drumkit = int(inputKit)
        validKit = True
    else:
        # Ask for input
        print(" Drumkit must be an integer smaller than 5")
        inputKit = input("Choose a drumkit: ")

# Load the chosen drumkit
sample0 = sa.WaveObject.from_wave_file("../audio/kik" + str(drumkit) + ".wav")
sample1 = sa.WaveObject.from_wave_file("../audio/snr" + str(drumkit) + ".wav")
sample2 = sa.WaveObject.from_wave_file("../audio/hhc" + str(drumkit) + ".wav")
sample3 = sa.WaveObject.from_wave_file("../audio/per" + str(drumkit) + ".wav")

samples = [sample0, sample1, sample2, sample3]

# Load a samplePlayer for each sample
players = []
for i in range(len(samples)):
    players.append(samplePlayer(i))

# Sequence of drumtriggers
seq0 = [1, 2, 0, 0, 2, 1, 0, 0]
seq1 = [0, 0, 1, 0, 0, 0, 1, 0]
seq2 = [1, 1, 1, 1, 1, 1, 1, 1]
seq3 = [0, 2, 0, 2, 2, 1, 2, 2]

sequences = [seq0, seq1, seq2, seq3]

# Set the BPM
validBPM = False
inputBPM = input("Choose a BPM: ")

# Check if BPM input is valid and try again if needed
while validBPM == False:
    if inputBPM.isdigit():
        # Set BPM, exit loop, start playback
        bpm = int(inputBPM)
        validBPM = True
        playback = True
    else:
        # Ask for input
        print(" BPM must be an integer.")
        inputBPM = input("Choose a BPM: ")

# Calculate timing values
trigCount = 0    # initial trigger
trigsPerBeat = 2 # triggers per quarter note
triggerLength = 60/bpm/trigsPerBeat
print("Duration of a single trigger:",triggerLength)
#time.sleep(60/bpm/trigsPerBeat)

# Play the beat
t0 = time.time()

while playback == True:
    if time.time() - t0 >= triggerLength:    
        # Send a trigger to each player with the triggers from the corresponding sequence
        for i in range(len(samples)):
            players[i].playSample(sequences[i][trigCount%8])

        t0 = time.time()
        trigCount += 1
#    else:
#        time.sleep(0.001)
