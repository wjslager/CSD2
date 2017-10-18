import sys

# Function which asks and then evaluates input
def askInput(low, high):
    inputValue = input('> ')

    # Loop until input is valid
    while True:
        if inputValue.isdigit() and high >= int(inputValue) >= low:
            return int(inputValue)
        else:
            # Try again
            print('Invalid input. Must be an integer ranging from', low, 'to', high, '\n')
            inputValue = input('> ')

# Funtion which evaluates given input
def checkInput(inputValue, low, high):
    if inputValue.isdigit() and high >= int(inputValue) >= low:
        return int(inputValue)
    else:
       print('Invalid input. Must be an integer ranging from', low, 'to', high, '\n')

def helpFile():
    # Prints the help file
    print('Overview of all commands\n')
    print('{:6}{:10}{}'.format('BPM', '<value>', 'Set new BPM to <value>. <value> must be an integer ranging from 50 to 200'))
    print('{:16}{}'.format('START', 'Starts (or restarts) playback from the beginning'))
    print('{:16}{}'.format('STOP', 'Stops playback\n'))
    print('{:6}{:10}{}'.format('EXIT', 'QUIT', 'Exits the program'))
    print('{:16}{}'.format('HELP', 'You already know what this does..\n'))

def exitProgram():
    print('BLEEP BLEEP SHUT DOWN')
    sys.exit()
