#include <iostream>
#include "simplesynth.h"
#include "oscillator.h"
#include "sinewave.h"
#include "squarewave.h"

SimpleSynth::SimpleSynth()
{
  oscillator.setFrequency(20, 48000);
}

SimpleSynth::~SimpleSynth()
{
}

void SimpleSynth::process(float *outputBufferRef)
{
  for (int i=0; i<256; i++) {
    outputBufferRef[i] = oscillator.getSample();
    oscillator.tick();
  }
}

// void SimpleSynth::setWaveform()
// {
//   // set new wavetype
// }
