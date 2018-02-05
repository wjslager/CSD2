import sys
import time
import os
import colors as col
import platform

# Print startup overview
def titleText():
    clearConsole()
    print(col.header+"IrRegular Beat Generator\n")
    print(col.info+"By Ward Slager, 2018\nType help for an overview of all commands\n")
    print(col.reset)

# Function which asks and then evaluates input in a specified range
def askInput(low, high):
    inputValue = input("> ")

    # Loop until input is valid
    while True:
        if inputValue.isdigit() and high >= int(inputValue) >= low:
            return int(inputValue)
        else:
            # Try again
            print(col.error+"Invalid input. Must be an integer ranging from", low, "to", high, col.reset)
            inputValue = input("> ")

# Funtion which evaluates given input in a specified range
def checkInput(inputValue, currentVAL, low, high):
    if inputValue.isdigit() and high >= int(inputValue) >= low:
        return int(inputValue)
    else:
       print(col.error+"Invalid input. Must be an integer ranging from", low, "to", high, col.reset)
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
          print(col.error+"Invalid input. Must be an integer:", valA, "or", valB, col.reset)
          inputValue = input("> ")

# Funtion which evaluates given input looking for specific values
def checkInputOr(inputValue, currentVAL, valA, valB):
    if inputValue.isdigit() and int(inputValue) == valA or int(inputValue) == valB:
        return int(inputValue)
    else:
       print(col.error+"Invalid input. Must be an integer:", valA, "or", valB, col.reset)
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
    clearConsole()

    # Print my nice snaredrum logo
    file = open("snaredrum.txt", "r")
    for line in file:
        print(line, end='')
    sys.exit()

def clearConsole():
    os.system('clear')
    os.system('cls')
