import sys
import time
import os
from colorama import deinit, Fore, Back, Style

# Error Color
erc = "\033[31m"

# Print startup overview
def titleText():
    clearConsole()
    print("\033[96m"+"_ ____ ____ ____ ____ _  _ _    ____ ____    ___  ____ ____ ___    ____ ____ _  _ ____ ____ ____ ___ ____ ____ \n| |__/ |__/ |___ | __ |  | |    |__| |__/    |__] |___ |__|  |     | __ |___ |\ | |___ |__/ |__|  |  |  | |__/ \n| |  \ |  \ |___ |__] |__| |___ |  | |  \    |__] |___ |  |  |     |__] |___ | \| |___ |  \ |  |  |  |__| |  \ \n")
    print("By Ward Slager, 2017\nType help for an overview of all commands\n")
    # print("_ _ _ ____ ____ ___     ____ _    ____ ____ ____ ____ \n| | | |__| |__/ |  \    [__  |    |__| | __ |___ |__/ \n|_|_| |  | |  \ |__/    ___] |___ |  | |__] |___ |  \ \n")

# Function which asks and then evaluates input in a specified range
def askInput(low, high):
    inputValue = input("> ")

    # Loop until input is valid
    while True:
        if inputValue.isdigit() and high >= int(inputValue) >= low:
            return int(inputValue)
        else:
            # Try again
            print(erc+"Invalid input. Must be an integer ranging from", low, "to", high)
            inputValue = input("> ")

# Funtion which evaluates given input in a specified range
def checkInput(inputValue, currentVAL, low, high):
    if inputValue.isdigit() and high >= int(inputValue) >= low:
        return int(inputValue)
    else:
       print(erc+"Invalid input. Must be an integer ranging from", low, "to", high)
       return currentVAL

# Function which asks and then evaluates input looking for specific values
def askInputOr(valA, valB):
  inputValue = input("> ")

  # Loop until input is valid
  while True:
      if inputValue.isdigit() and int(inputValue) == valA or int(inputValue) == valB:
          return int(inputValue)
      else:
          # Try again
          print(erc+"Invalid input. Must be an integer:", valA, "or", valB)
          inputValue = input("> ")

# Funtion which evaluates given input looking for specific values
def checkInputOr(inputValue, currentVAL, valA, valB):
    if inputValue.isdigit() and int(inputValue) == valA or int(inputValue) == valB:
        return int(inputValue)
    else:
       print(erc+"Invalid input. Must be an integer:", valA, "or", valB)
       return currentVAL

# Print command overview
def helpFile():
    print("Overview of all commands\n")
    print("{:14}{}".format("START", "(re)starts playback from the beginning"))
    print("{:14}{}".format("STOP", "stops playback\n"))

    print("{:14}{}".format("GEN", "(re)generates a beat\n"))
    print("{:14}{}".format("GENP", "(re)generates a beat and print the result\n"))

    print("{:14}{}".format("", "The following commands only go into effect after restarting playback (and regeneration):"))
    print("{:10}{:4}{}".format("BPM", "$", "set BPM to $. (50-200)"))
    print("{:10}{:4}{}".format("TIME", "$", "set triggers per measure to $. (4-12)"))
    print("{:10}{:4}{}".format("QUARTER", "$", "set triggers per quarter note to $. (1-4)\n"))
    print("{:10}{:4}{}".format("KIT", "$", "set drumkit to $. (0-1)\n"))

    print("{:14}{}".format("PRINT", "print the current beat"))
    print("{:10}{:4}{}".format("MIDI", "$", "write midi file with filename $.\n"))
    print("{:14}{}".format("HELP", "you already know what this does.."))
    print("{:7}{:7}{}".format("EXIT", "QUIT", "self-explanatory\n"))

# Exits the program
def exitProgram():
    # Exit colorama
    deinit()

    # clearConsole()
    # titleText()
    # ufo()

    # Print my nice snaredrum logo
    file = open("snaredrum.txt", "r")
    for line in file:
        print(line, end='')
    sys.exit()

def clearConsole():
    # Try to clear using clear, and then cls on windows systems
    # This is done because when using cygwin (or other emulators)
    # os.name=='nt' will return true while it still does not react cls
    # By using clear first and then cls on windows systems this
    # sort of fixes the problem
    os.system('clear')
    if os.name=='nt':
        os.system('cls')


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
