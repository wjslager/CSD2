import time
import simpleaudio as sa
import beatGenerator as bgen
import random
import colors as col

timingPrint = False

# Function which loads the samples
def loadSamples():
    global samples, sounds

    sample0 = sa.WaveObject.from_wave_file("audio/kik" + str(drumkit).zfill(3) + ".wav")
    sample1 = sa.WaveObject.from_wave_file("audio/snr" + str(drumkit).zfill(3) + ".wav")
    sample2 = sa.WaveObject.from_wave_file("audio/hhc" + str(drumkit).zfill(3) + ".wav")

    samples = [sample0, sample1, sample2]

    # Load a samplePlayer for each sample
    sounds = []
    for i in range(3):
        sounds.append(samplePlayer(i))

# Class which plays a single sample
class samplePlayer:
    global samples

    def __init__(self, sample=0):
        # Each instance only plays one sample
        # Store which sample this instance will play
        # sampleIndex values:
        # 0 Kick
        # 1 Snare
        # 2 HiHats
        self.sampleIndex = sample

    def playSample(self, trig):
        self.trig = trig

        if trig == 1:
            # Normal trigger
            samples[self.sampleIndex].play()

        elif trig == 2:
            if random.randint(0, 1) == 1:
                # Random trigger (doesn"t always trigger)
                samples[self.sampleIndex].play()

# Function which initializes all variables needed for playback
def initPlayback(bpm, printInfo=False):
    global timeQuarter, trigCount, triggerLength, playbackStart, playback, timing

    trigCount = 0
    triggerLength = 60/bpm/timeQuarter

    # Save time used for checking timing inbetween notes, only used for debugging
    timing = time.time()

    # Only prints info if specifically asked for (i.e. when debugging)
    if printInfo:
        print(col.info + "Initializing playback \n- A measure has", timeBeats, "triggers\n- A single trigger takes", int(1000*triggerLength), "ms\n-", timeQuarter, "triggers per quarter note\n" + col.reset)

    playbackStart = time.time()
    playback = True

# Thread which plays the sequences
def playbackThread():
    global playbackStart, trigCount, triggerLength, timing, timingPrint, timeBeats

    # This loop makes sure the thread doesn't stop even though playback can stop
    while True:
        while playback == True:
            # Calculates at which exact time the next event should play
            nextTriggerTime = playbackStart + trigCount * triggerLength

            if time.time() >= nextTriggerTime:
                # Send a trigger to each player with the triggers from the corresponding sequence
                for i in range(len(samples)):
                    sounds[i].playSample(bgen.sequences[i][trigCount%timeBeats])

                trigCount += 1

                # Only used for checking timing, not required for playback
                if timingPrint:
                    print(trigCount, int(1000*(time.time()-timing)), "ms")
                    timing = time.time()

            else:
                # Wait 10ms before checking again
                time.sleep(0.01)
