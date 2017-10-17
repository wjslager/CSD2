import simpleaudio as sa
import time
import random
import _thread
import sys

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

# Function which initializes all variables needed for playback
def initPlayback(bpm):
    global trigCount, trigsPerBeat, triggerLength, playbackStart, playback
    
    trigCount = 0
    trigsPerBeat = 4
    triggerLength = 60/bpm/trigsPerBeat
    print('Initializing playback \n- A single trigger takes', int(1000*triggerLength), 'ms\n-', trigsPerBeat, 'triggers per quarter note\n')

    playbackStart = time.time()
    playback = True

# Function which asks and then evaluates input
def askInput(low, high):
    inputValue = input('> ')
    
    while True:
        if inputValue.isdigit() and high >= int(inputValue) >= low:
            return int(inputValue)
        else:
            # Try again
            print('Invalid input. Must be an integer ranging from', low, 'to', high, '\n')
            inputValue = input('> ')

# Funtion which evaluates input
def checkInput(inputValue, low, high):
    if inputValue.isdigit() and high >= int(inputValue) >= low:
        return int(inputValue)
    else:
       print('Invalid input. Must be an integer ranging from', low, 'to', high, '\n') 

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
                #print(trigCount, int(1000*(time.time()-timing)), 'ms')
                timing = time.time()
                
            else:
                # Wait 10ms before checking again
                time.sleep(0.01)

def exitProgram():
    print('Quitting the program')
    time.sleep(0.1)
    sys.exit()

def helpFile():
    print('Overview of all commands')
    print('{:15}{}'.format('BPM <value>', 'Change the BPM. Value must be an integer ranging from 50 to 200'))
    print('{:15}{}'.format('EXIT', 'Self explanatory\n'))  

# = == === ==== ===== ====== # Playback preparations # ====== ===== ==== === == = #

# Drumkit selection
print('Available drumkits: \n 0: Synthetic \nChoose a drumkit: \n')
drumkit = askInput(0, 0)

# Load the chosen drumkit
sample0 = sa.WaveObject.from_wave_file('kik' + str(drumkit).zfill(3) + '.wav')
sample1 = sa.WaveObject.from_wave_file('snr' + str(drumkit).zfill(3) + '.wav')
sample2 = sa.WaveObject.from_wave_file('hhc' + str(drumkit).zfill(3) + '.wav')

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

print('Choose a BPM: \n')
bpm = askInput(50, 200)

# = == === ==== ===== ====== # Playback Loop # ====== ===== ==== === == = #

# Save time used for checking timing inbetween notes
timing = time.time()

# Calculates the length of triggers
initPlayback(bpm)

# Start the playback loop
try:
   _thread.start_new_thread(playbackThread, ())
except:
   print('Error: unable to start thread \n')

# Check for keyboard input
while True:
    userInput = input('> ')

    # Splits input into a list, allows evaluating indiviual words
    userInput = userInput.split(' ', 1)

    if userInput[0].lower() == 'exit':
        exitProgram()
    elif userInput[0].lower() == 'bpm':
        bpm = checkInput(userInput[1], 50, 200)
    elif userInput[0].lower() == 'help':
        helpFile()
    else:
        print(' '.join(userInput),'not recognized, type help for an overview of all commands \n')
