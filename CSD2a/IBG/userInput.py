import sys
import time
import os

# Print startup overview
def startupInfo():
    print("_ ____ ____ ____ ____ _  _ _    ____ ____    ___  ____ ____ ___    ____ ____ _  _ ____ ____ ____ ___ ____ ____ \n| |__/ |__/ |___ | __ |  | |    |__| |__/    |__] |___ |__|  |     | __ |___ |\ | |___ |__/ |__|  |  |  | |__/ \n| |  \ |  \ |___ |__] |__| |___ |  | |  \    |__] |___ |  |  |     |__] |___ | \| |___ |  \ |  |  |  |__| |  \ \n\n")
    print("_ _ _ ____ ____ ___     ____ _    ____ ____ ____ ____ \n| | | |__| |__/ |  \    [__  |    |__| | __ |___ |__/ \n|_|_| |  | |  \ |__/    ___] |___ |  | |__] |___ |  \ \n")

# Function which asks and then evaluates input
def askInput(low, high):
    inputValue = input("> ")

    # Loop until input is valid
    while True:
        if inputValue.isdigit() and high >= int(inputValue) >= low:
            return int(inputValue)
        else:
            # Try again
            print("Invalid input. Must be an integer ranging from", low, "to", high, "\n")
            inputValue = input("> ")

# Funtion which evaluates given input
def checkInput(inputValue, currentBPM, low, high):
    if inputValue.isdigit() and high >= int(inputValue) >= low:
        return int(inputValue)
    else:
       print("Invalid input. Must be an integer ranging from", low, "to", high, "\n")
       return currentBPM

# Print command overview
def helpFile():
    print("Overview of all commands\n")
    print("{:6}{:10}{}".format("BPM", "<value>", "Set new BPM to <value>. <value> must be an integer ranging from 50 to 200"))
    print("{:16}{}".format("START", "Starts (or restarts) playback from the beginning"))
    print("{:16}{}".format("STOP", "Stops playback\n"))
    print("{:6}{:10}{}".format("EXIT", "QUIT", "Exits the program"))
    print("{:16}{}".format("HELP", "You already know what this does..\n"))

# Exits the program and DESTROYS ALL THE EARTHLINGS!!
def exitProgram():
    clearConsole()
    ufo()
    sys.exit()

def clearConsole():
    os.system('cls' if os.name=='nt' else 'clear')

def ufo():
    print("SURRENDER EARTHLINGS!")
    time.sleep(0.5)
    print("YOU WILL NOT ESCAPE YOUR FATE!")
    time.sleep(0.5)
    print("       _______")
    print("      / O O O \ ")
    print("      \_______/ ")
    time.sleep(0.1)
    print("          .")
    time.sleep(0.05)
    print("         ...")
    time.sleep(0.05)
    print("        .....")
    time.sleep(0.05)
    print("       . ... .")
    time.sleep(0.05)
    print("      . . . . .")
    time.sleep(0.05)
    print("     . .  .  . .")
    time.sleep(0.05)
    print("    . . . . . . .")
    time.sleep(0.05)
    print("   . . .  .  . . .")
    time.sleep(0.05)
    print("  . . . . . . . . .")
    time.sleep(0.05)
    print(" . . . .  .  . . . .")
    time.sleep(0.05)
    print(". . . . . . . . . . .")
