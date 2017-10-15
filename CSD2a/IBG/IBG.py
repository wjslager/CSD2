# CHECKLIST
# - Option to input each list at booting the program
# - Add variation over time: list manipulation
#       if interval has passed else wait a ~10ms
# - check all files ending with *.wav -> laad deze

# ISSUES
# - Clicks when samples are retriggered
# - Timing inbetween triggers is sloppy


import simpleaudio as sa
import time
import random

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
    global playbackStart, trigCount, triggerLength
    
    trigCount = 0
    trigsPerBeat = 4
    triggerLength = 60/bpm/trigsPerBeat
    print(" Initializing playback \n - A single trigger takes", int(1000*triggerLength), "ms\n -", trigsPerBeat, "triggers per quarter note")

    playbackStart = time.time()

# Drumkit selection
validKit = False
print("1: Synthetic \n2: n/a \n3: n/a")
inputKit = input("Choose a drumkit: ")

# Check if drumkit input is valid and try again if needed
while validKit == False:
    if inputKit.isdigit() and int(inputKit) < 4:
        # Set Kit, exit loop
        drumkit = int(inputKit)
        validKit = True
    else:
        # Try again
        print(" Drumkit must be an integer smaller than 5")
        inputKit = input("Choose a drumkit: ")

# Load the chosen drumkit
sample0 = sa.WaveObject.from_wave_file("kik" + str(drumkit-1) + ".wav")
sample1 = sa.WaveObject.from_wave_file("snr" + str(drumkit-1) + ".wav")
sample2 = sa.WaveObject.from_wave_file("hhc" + str(drumkit-1) + ".wav")

samples = [sample0, sample1, sample2]

# Load a samplePlayer for each sample
sounds = []
for i in range(len(samples)):
    sounds.append(samplePlayer(i))

# Sequence of drumtriggers
seq0 = [1, 0, 0, 0, 1, 0, 0, 0]
seq1 = [0, 0, 0, 0, 1, 0, 0, 0]
seq2 = [0, 2, 1, 2, 0, 2, 1, 2]

sequences = [seq0, seq1, seq2]

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
        # Try again
        print(" BPM must be an integer.")
        inputBPM = input("Choose a BPM: ")


initPlayback(bpm)

# Save time used for checking timing inbetween notes
timing = time.time()

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
            print(trigCount, int(1000*(time.time()-timing)), "ms")
            timing = time.time()
            
        else:
            # Wait 10ms before checking again
            time.sleep(0.01)
