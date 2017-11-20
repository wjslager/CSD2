from midiutil.MidiFile import MIDIFile
from midiutil import MIDIFile

# http://midiutil.readthedocs.io/en/stable/
# https://pypi.python.org/pypi/MIDIUtil/.

def writeMidi(sequences, filename, bpm, timeQuarter, timeBeats):
    track    = 0
    #used midi channel
    channel  = 9
    #set time, in beats
    time     = 0
    #set timeQuarter in beats, 0.5 -> .../8 time signature
    duration = 1/timeQuarter

    # Initalize MIDIUtil stuff
    MyMIDI = MIDIFile(2, adjust_origin=True)

    # Add a BPM track
    MyMIDI.addTempo(track, time, bpm)

    # Set the time signatures
    # Denominator values are:
    # 2 = */4 time signatures
    # 3 = */8 time signatures
    if timeBeats == 4 or timeBeats == 8:
        # Just do 4/4 (prevents 8/8 time signatures)
        numerator = 4
        denominator = 2
    else:
        # Let the computer work it out
        numerator = timeBeats
        denominator = int((timeQuarter*0.5) + 1)
    MyMIDI.addTimeSignature(track, 0, numerator, denominator, 24)

    # Each beat will only have material for half a measure
    # This copies the first half into the empty second half
    kikTrigs = sequences[0] + sequences[0]
    snrTrigs = sequences[1] + sequences[1]
    hhcTrigs = sequences[2] + sequences[2]

    # Check for triggers
    # Normal triggers (1) will result in a note at velocity 127
    # Random triggers (2) will result in a note at velocity 63
    for i in range(timeBeats*2):
        if kikTrigs[i] >= 1:
            velocity = (kikTrigs[i] *-64) + 191
            MyMIDI.addNote(track, channel, 36, i * duration, duration, velocity)
        if snrTrigs[i] >= 1:
            velocity = (snrTrigs[i] *-64) + 191
            MyMIDI.addNote(track, channel, 38, i * duration, duration, velocity)
        if hhcTrigs[i] >= 1:
            velocity = (hhcTrigs[i] *-64) + 191
            MyMIDI.addNote(track, channel, 42, i * duration, duration, velocity)

    # Modify given filename to write the file inside of the midi folder
    filename = "midi/"+filename

    #write to MIDIfile
    with open(filename+".mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)

    print(" midi written to", filename+".mid\n")
