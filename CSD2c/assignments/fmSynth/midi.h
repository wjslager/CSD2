#ifndef _MIDI_H_
#define _MIDI_H_

#include <cmath>

// Convert midi to frequency in hz
float mtof(float midiNote)
{
  return pow(2, (midiNote - 69) / 12) * 440;
}

#endif
