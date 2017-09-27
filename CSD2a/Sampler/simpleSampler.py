# TODO
# - Option to input each list at booting the program
# - Make a sample playing class allowing more sounds to be used without copy-pasting code

# ISSUES
# - Samples are cutoff when a new sample is triggered

import simpleaudio as sa
import time

kickWav = sa.WaveObject.from_wave_file("kick.wav")
snareWav = sa.WaveObject.from_wave_file("snare.wav")
hhWav = sa.WaveObject.from_wave_file("hh.wav")

# Lists with drumtriggers
kickTrig =  [1, 0, 0, 0, 1, 1, 0, 0]
snareTrig = [0, 0, 1, 0, 0, 0, 0, 1]
hhTrig =    [1, 1, 1, 1, 1, 1, 1, 1]

trigCount = 0
trigsPerBeat = 2

# Ask for input and check if input is usable as BPM
validBPM = False
inputBPM = input("Enter BPM: ")

while validBPM == False:
    if inputBPM.isdigit():
        # Set BPM, exit loop, start playback
        bpm = int(inputBPM)
        validBPM = True
        playback = True
    else:
        # Ask for input
        print(" BPM must be an integer.")
        inputBPM = input("Enter BPM: ")

print("BPM is", bpm)

# Check lists for each sound
while playback == True :
    if kickTrig[trigCount%8] == 1:
        playObj = kickWav.play()

    if snareTrig[trigCount%8] == 1:
        playObj = snareWav.play()

    if hhTrig[trigCount%8] == 1:
        playObj = hhWav.play()
       
    time.sleep(60/bpm/trigsPerBeat)
    trigCount += 1
