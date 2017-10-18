import simpleaudio as sa
import time
import random
import _thread
import sys
import userInput as ui
import playback as pb

# = == === ==== ===== # Playback preparations # ===== ==== === == = #

# Drumkit selection
print("Available drumkits: \n 0: Synthetic \nChoose a drumkit: \n")
pb.drumkit = ui.askInput(0, 0)

# Load the chosen drumkit
pb.loadSample()

print("Choose a BPM: \n")
bpm = ui.askInput(50, 200)

# = == === ==== ===== # Playback Loop # ===== ==== === == = #

# Save time used for checking timing inbetween notes, only used for debugging
timing = time.time()

# Calculates the length of triggers and display info
pb.initPlayback(bpm, True)

# Start the playback thread
try:
   _thread.start_new_thread(pb.playbackThread, ())
except:
   print("Error: unable to start thread \n")

while True:
    # Wait for keyboard input
    userInput = input("> ")

    # Splits input into a list, allows evaluating indiviual words
    userInput = userInput.split(" ", 1)

    # Exit program
    if userInput[0].lower() == "exit" or userInput[0].lower() == "quit":
        ui.exitProgram()

    # Settings
    elif userInput[0].lower() == "bpm":
        bpm = ui.checkInput(userInput[1], 50, 200)

    # Show help file
    elif userInput[0].lower() == "help":
        ui.helpFile()

    # Start or restart playback
    elif userInput[0].lower() == "start":
        pb.initPlayback(bpm)
        pb.playback = True

    # Stop playback
    elif userInput[0].lower() == "stop":
        if pb.playback:
            pb.playback = False
        else:
            print("Playback has already stopped \n")

    # Command not recognized
    else:
        print(" ".join(userInput),"not recognized, type help for an overview of all commands \n")
