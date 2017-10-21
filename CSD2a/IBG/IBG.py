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
ui.startupInfo()

# = == === ==== ===== # Initialize values # ===== ==== === == = #

# Initial settings selection.
# Settings can be changed afterwards, but values are needed to:
# - Load the samples
# - initialize playback

# Drumkit selection
print("Available drumkits: \n 0: Synthetic \n\nChoose a drumkit:")
pb.drumkit = ui.askInput(0, 0)

# Load all the samples of the drumkit
pb.loadSamples()

# Time signature selection
print("\nHow many triggers per measure? (4-12)")
pb.timeBeats = ui.askInput(4, 12)

pb.timeMeasure = 2
# print("\nHow many triggers per quarter note? (2-2)")
# pb.timeMeasure = ui.askInput(2, 2)

# BPM selection
print("\nChoose a BPM: ")
bpm = ui.askInput(50, 200)

# Generate the actual beat
# First boolean determines if the beat is actually generated
# False will just play a predefined sequence consisting of 8 triggers
bgen.generate(True, pb.timeBeats, pb.timeMeasure)

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
        ui.exitProgram()

    # Settings
    elif userInput[0].lower() == "bpm":
        bpm = ui.checkInput(userInput[1], bpm, 50, 200)

    # Show help file
    elif userInput[0].lower() == "help":
        ui.helpFile()

    # Generate a beat
    elif userInput[0].lower() == "generate":
        bgen.generate(True, pb.timeBeats, pb.timeMeasure)

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
