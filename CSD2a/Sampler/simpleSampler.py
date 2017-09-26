#TODO play a sound

import simpleaudio as sa
import time

kickWav = sa.WaveObject.from_wave_file("kick.wav")
snareWav = sa.WaveObject.from_wave_file("snare.wav")
hhWav = sa.WaveObject.from_wave_file("hh.wav")

kickTrig =  [1, 0, 0, 0, 1, 1, 0, 0]
snareTrig = [0, 0, 1, 0, 0, 0, 0, 1]
hhTrig =    [1, 1, 1, 1, 1, 1, 1, 1]

trigCount = 0
bpm = 120

print("BPM is", bpm)
while True :
    print("trigPos is", trigCount%8)

    if kickTrig[trigCount%8] == 1:
        play_obj = kickWav.play()

    if snareTrig[trigCount%8] == 1:
        play_obj = snareWav.play()

    time.sleep(0.01) 
    if hhTrig[trigCount%8] == 1:
        play_obj = hhWav.play()
        
    time.sleep(0.2)
    trigCount += 1

# play_obj.wait_done()
# heb ik dit nodig??
