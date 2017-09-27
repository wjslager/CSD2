# TODO
# - Triggering the samples with a class
# - Option to input each list at booting the program
# - Make a sample playing class allowing more sounds to be used without copy-pasting code

# ISSUES
# - Samples are cutoff when a new sample is triggered (clicky)

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
                # Random trigger
                playObj = samples[self.sampleIndex].play()


print(" / / / / simpleSampler / / / / ")

# Drumkit selection
validKit = False
print("1: Tape")
print("2: 808")
print("3: 909")
print("4: DMX")
inputKit = input("Drumkit: ")

# Check if drumkit input is valid and try again if needed
while validKit == False:
    if inputKit.isdigit() and int(inputKit) < 5:
        # Set Kit, exit loop
        drumkit = int(inputKit)
        validKit = True
    else:
        # Ask for input
        print(" Drumkit must be an integer smaller than 5")
        inputKit = input("Drumkit: ")

# Load the chosen drumkit
sample0 = sa.WaveObject.from_wave_file("kik" + str(drumkit) + ".wav")
sample1 = sa.WaveObject.from_wave_file("snr" + str(drumkit) + ".wav")
sample2 = sa.WaveObject.from_wave_file("hhc" + str(drumkit) + ".wav")
sample3 = sa.WaveObject.from_wave_file("per" + str(drumkit) + ".wav")

samples = [sample0, sample1, sample2, sample3]

# Load a samplePlayer for each sample
players = []
for i in range(len(samples)):
    players.append(samplePlayer(i))

# Sequence of drumtriggers
seq0 = [1, 0, 0, 0, 1, 1, 2, 0]
seq1 = [0, 0, 1, 0, 0, 0, 2, 1]
seq2 = [1, 1, 1, 1, 1, 1, 1, 1]
seq3 = [0, 1, 0, 1, 0, 1, 0, 1]

sequences = [seq0, seq1, seq2, seq3]

# Grid
trigCount = 0 
trigsPerBeat = 2

# Set the BPM
validBPM = False
inputBPM = input("BPM: ")

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
        inputBPM = input("BPM: ")
    
while playback == True :    
    # Send a trigger to each player with the triggers from the corresponding sequence
    for i in range(len(samples)):
        players[i].playSample(sequences[i][trigCount%8])

    # Wait for the next trigger
    time.sleep(60/bpm/trigsPerBeat)
    trigCount += 1
