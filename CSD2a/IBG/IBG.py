# Python modules
import simpleaudio as sa
import time
import random
import _thread
import sys
from colorama import init, Fore, Back, Style

# Project modules
import userInput as ui
import playback as pb
import beatGenerator as bgen
import writeMidi as midi

# Error Color
erc = "\033[31m"

# Initialize colorama
init(autoreset=True)

# Display some nice things
ui.titleText()

# = == === ==== ===== # Initialize values # ===== ==== === == = #

# Initial settings selection.
# Settings can be changed afterwards, but values are needed to:
# - Load the samples
# - Start playback

totalDrumkits = 4
totalDrumkits -= 1 # Compensate for the filenames starting at 0

# Drumkit selection
print("Available drumkits: \n 0: Dry \n 1: Synthetic \n 2: Dub \n 3: Beatboxing \n\nChoose a drumkit:")
pb.drumkit = ui.askInput(0, totalDrumkits)

# Load all the samples of the drumkit
pb.loadSamples()

# Time signature selection
print("\nHow many triggers per measure? (4-12)")
pb.timeBeats = ui.askInput(4, 12)

print("\nHow many triggers per quarter note? (2 or 4)")
pb.timeQuarter = ui.askInputOr(2, 4)
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
   print(erc+"Error: unable to start thread \n")

askForInput = True
prevUserInput = None

# Loop checking for user input
while True:

    # Wait for keyboard input
    userInput = input("> ")

    # Splits input into a list, allows evaluating indiviual words
    userInput = userInput.split(" ", 1)

    # Empty input or a space will repeat the last command
    if userInput[0] == "":
        if not prevUserInput == None:
            print(" Repeating:", ' '.join(prevUserInput))
            userInput = prevUserInput

    # Exit program
    if userInput[0].lower() in ["exit", "quit", "e"]:
    # if userInput[0].lower() == "exit" or userInput[0].lower() == "quit" or userInput[0].lower() == "e":
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
            print(erc+"Playback has already stopped \n")

    # Trigger the generation engine
    elif userInput[0].lower() == "gen":
        bgen.generate(pb.timeBeats, pb.timeQuarter)

    # Trigger the generation engine and print the result
    elif userInput[0].lower() == "genp":
        bgen.generate(pb.timeBeats, pb.timeQuarter)
        hhcPrint = " ".join(str(i) for i in bgen.sequences[2])
        snrPrint = " ".join(str(i) for i in bgen.sequences[1])
        kikPrint = " ".join(str(i) for i in bgen.sequences[0])
        print("  Hihats:", hhcPrint.replace("0", "-"))
        print("  Snare: ", snrPrint.replace("0", "-"))
        print("  Kick:  ", kikPrint.replace("0", "-"))

    # BPM
    elif userInput[0].lower() == "bpm":
        if len(userInput) <= 1:
            print(erc+" ! Missing argument: \n  expecting bpm + value")
        else:
            bpm = ui.checkInput(userInput[1], bpm, 50, 200)

    # Time signature
    elif userInput[0].lower() == "time":
        if len(userInput) <= 1:
            print(erc+" ! Missing argument: \n  expecting time + value")
        else:
            pb.timeBeats = ui.checkInput(userInput[1], pb.timeBeats, 4, 12)
            if userInput[1].isdigit() and 12 >= int(userInput[1]) >= 4:
                pb.playback = False
                bgen.generate(pb.timeBeats, pb.timeQuarter)
            pb.timeBeats = ui.checkInput(userInput[1], pb.timeBeats, 4, 12)

    # Quarter notes resolution
    elif userInput[0].lower() == "quarter":
        if len(userInput) <= 1:
            print(erc+" ! Missing argument: \n  expecting quarter + value")
        else:
            pb.timeQuarter = ui.checkInputOr(userInput[1], pb.timeQuarter, 2, 4)

    # Drumkit
    elif userInput[0].lower() == "kit":
        if len(userInput) <= 1:
            print(erc+" ! Missing argument: \n  expecting drumkit + value")
        else:
            pb.drumkit = ui.checkInput(userInput[1], pb.drumkit, 0, totalDrumkits)
            # If value is valid: load selected drumkit
            if userInput[1].isdigit() and totalDrumkits >= int(userInput[1]) >= 0:
                pb.loadSamples()

    # Print current sequences
    elif userInput[0].lower() == "print":
        hhcPrint = " ".join(str(i) for i in bgen.sequences[2])
        snrPrint = " ".join(str(i) for i in bgen.sequences[1])
        kikPrint = " ".join(str(i) for i in bgen.sequences[0])
        print("  Hihats:", hhcPrint.replace("0", "-"))
        print("  Snare: ", snrPrint.replace("0", "-"))
        print("  Kick:  ", kikPrint.replace("0", "-"))

    # Write beat to midi file
    elif userInput[0].lower() == "midi":
        # Set filename if not specified
        if len(userInput) <= 1:
            print(erc+" ! Missing argument:\n  filename set to irregbeat.mid")
            userInput.append("irregbeat")
        # Write midifile
        midi.writeMidi(bgen.sequences, userInput[1], bpm, pb.timeQuarter, pb.timeBeats)

    # Show help file
    elif userInput[0].lower() == "help":
        ui.helpFile()

    # SPOOKY
    elif userInput[0].lower() == "ufo":
        ui.ufo()

    # Command not recognized
    else:
        print(erc+" ".join(userInput), erc+"not recognized, type help for an overview of all commands \n")

    prevUserInput = userInput
