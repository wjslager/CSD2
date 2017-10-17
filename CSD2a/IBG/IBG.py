# CHECKLIST
# - Option to input each list at booting the program (or load from disk)
# - Add variation over time: list manipulation
# - Check all files ending with *.wav and load them

# ISSUES
# - Clicks when samples are retriggered
# - Timing inbetween triggers is sloppy

import simpleaudio as sa
import time
import random
import _thread
import sys
from sys import stdin

# = == === ===== ======  # Classes and functions # ====== ===== ==== === == = #

# Class which plays a single sample
class samplePlayer:
    def __init__(self, sample=0):
        # Each instance only plays one sample
        # Store which sample this instance will play
        self.sampleIndex = sample
        
    def playSample(self, trig):
        self.trig = trig
        
        if trig == 1:
            # Normal trigger
            samples[self.sampleIndex].play()
            
        elif trig == 2:
            if random.randint(0, 1) == 1:
                # Random trigger (doesn't always trigger)
                samples[self.sampleIndex].play()

# Functions which initializes all variables needed for playback
def initPlayback(bpm):
    global trigCount, trigsPerBeat, triggerLength, playbackStart, playback
    
    trigCount = 0
    trigsPerBeat = 4
    triggerLength = 60/bpm/trigsPerBeat
    print("Initializing playback \n- A single trigger takes", int(1000*triggerLength), "ms\n-", trigsPerBeat, "triggers per quarter note")

    playbackStart = time.time()
    playback = True

# Functions which validates input values
def checkInput(low, high):
    inputValue = input("> ")
    
    while True:
        if inputValue.isdigit() and int(inputValue) >= low and int(inputValue) <= high:
            return int(inputValue)
        else:
            # Try again
            print("Invalid input. Must be an integer ranging from", low, "to", high)
            inputValue = input("> ")

# Thread which plays the sequences    
def playbackThread():
    global playbackStart, trigCount, triggerLength, timing
    
    while True:
        while playback == True:
            # Calculates at which exact time the next event should play
            nextTriggerTime = playbackStart + trigCount * triggerLength

            if time.time() >= nextTriggerTime:
                # Send a trigger to each player with the triggers from the corresponding sequence
                for i in range(len(samples)):
                    sounds[i].playSample(sequences[i][trigCount%8])

                trigCount += 1

                # Only used for checking timing, not required for playback
                #print(trigCount, int(1000*(time.time()-timing)), "ms")
                timing = time.time()
                
            else:
                # Wait 10ms before checking again
                time.sleep(0.01)

# = == === ==== ===== ====== # Playback preparations # ====== ===== ==== === == = #

# Ask for drumkit selection
# Load corresponding samples
# Initialize a sample player for each sample
# Define base patterns
# Ask for BPM input
# Initialize playback

# Drumkit selection
print("Available drumkits: \n 0: Synthetic \nChoose a drumkit: ")
drumkit = checkInput(0, 0)

print(drumkit)

# Load the chosen drumkit
sample0 = sa.WaveObject.from_wave_file("kik" + str(drumkit).zfill(3) + ".wav")
sample1 = sa.WaveObject.from_wave_file("snr" + str(drumkit).zfill(3) + ".wav")
sample2 = sa.WaveObject.from_wave_file("hhc" + str(drumkit).zfill(3) + ".wav")

samples = [sample0, sample1, sample2]

# Load a samplePlayer for each sample
sounds = []
for i in range(len(samples)):
    sounds.append(samplePlayer(i))

# Sequence of drumtriggers
# 0 no trigger
# 1 normal trigger, plays a sound
# 2 random trigger, sometimes plays a sound
seq0 = [1, 0, 0, 0, 1, 0, 0, 0]
seq1 = [0, 0, 0, 0, 1, 0, 0, 0]
seq2 = [0, 1, 1, 1, 0, 1, 1, 1]

sequences = [seq0, seq1, seq2]

print("Choose a BPM: ")
bpm = checkInput(50, 200)

# = == === ==== ===== ====== # Playback Loop # ====== ===== ==== === == = #

# Save time used for checking timing inbetween notes
timing = time.time()

# Calculates the length of triggers
initPlayback(bpm)

try:
   _thread.start_new_thread(playbackThread, ())
except:
   print("Error: unable to start thread")

while True:
  userInput = sys.stdin.read(1)
  if userInput == 'q':
    print("User typed q. Leaving program.")
    sys.exit()
  time.sleep(0.1)


