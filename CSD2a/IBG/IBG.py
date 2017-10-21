# Python modules
import simpleaudio as sa
import time
import random
import _thread
import sys

# Project modules
import userInput as ui
import playback as pb
import beatGenerator as bgen

# Display some nice things
ui.titleText()

# = == === ==== ===== # Initialize values # ===== ==== === == = #

# Initial settings selection.
# Settings can be changed afterwards, but values are needed to:
# - Load the samples
# - Start playback

# Drumkit selection
print("Available drumkits: \n 0: Synthetic \n\nChoose a drumkit: (0-0)")
pb.drumkit = ui.askInput(0, 0)

# Load all the samples of the drumkit
pb.loadSamples()

# Time signature selection
print("\nHow many triggers per measure? (4-12)")
pb.timeBeats = ui.askInput(4, 12)

print("\nHow many triggers per quarter note? (1-4)")
pb.timeQuarter = ui.askInput(1, 4)
# pb.timeQuarter = 2

# BPM selection
print("\nChoose a BPM: (50-200)")
bpm = ui.askInput(50, 200)

# Generate the actual beat
# First boolean determines if the beat is actually generated
# False will just play a predefined sequence consisting of 8 triggers
bgen.generate(pb.timeBeats, pb.timeQuarter)

# Calculates the length of triggers and display info
pb.initPlayback(bpm, True)

# = == === ==== ===== # Playback Loop # ===== ==== === == = #

# Start the playback thread
try:
   _thread.start_new_thread(pb.playbackThread, ())
except:
   print("Error: unable to start thread \n")

# Loop checking for user input
while True:
    # Wait for keyboard input
    userInput = input("> ")

    # Splits input into a list, allows evaluating indiviual words
    userInput = userInput.split(" ", 1)

    # Exit program
    if userInput[0].lower() == "exit" or userInput[0].lower() == "quit" or userInput[0].lower() == "e":
        pb.playback = False
        ui.exitProgram()

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

    # Trigger the generation engine
    elif userInput[0].lower() == "gen":
        bgen.generate(pb.timeBeats, pb.timeQuarter)

    # BPM
    elif userInput[0].lower() == "bpm" and len(userInput) > 1:
        bpm = ui.checkInput(userInput[1], bpm, 50, 200)
    elif userInput[0].lower() == "bpm":
        print(" ! Missing argument: \n  expecting bpm + value")

    # Time signature
    elif userInput[0].lower() == "time" and len(userInput) > 1:
        # If value is valid, stop playback to prevent issues
        if 12 >= int(userInput[1]) >= 4:
            pb.playback = False
            # bgen.generate(pb.timeBeats, pb.timeQuarter)
        pb.timeBeats = ui.checkInput(userInput[1], pb.timeBeats, 4, 12)
    elif userInput[0].lower() == "time":
        print(" ! Missing argument: \n  expecting time + value")

    # Quarter notes resolution
    elif userInput[0].lower() == "quarter" and len(userInput) > 1:
        pb.timeQuarter = ui.checkInput(userInput[1], pb.timeQuarter, 1, 4)
    elif userInput[0].lower() == "quarter":
        print(" ! Missing argument: \n  expecting quarter + value")

    # Show help file
    elif userInput[0].lower() == "help":
        ui.helpFile()

    # Ignore empty input.
    # This prevents filling the commandline with unnecessary error messages
    elif userInput[0] == "":
        pass

    # Command not recognized
    else:
        print(" ".join(userInput),"not recognized, type help for an overview of all commands \n")
