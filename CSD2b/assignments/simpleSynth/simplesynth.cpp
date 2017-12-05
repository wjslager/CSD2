#include <iostream>
#include "simplesynth.h"
#include "oscillator.h"
#include "sinewave.h"
#include "squarewave.h"

SimpleSynth::SimpleSynth()
{
  SineWave sine;
  SquareWave square;
}

SimpleSynth::~SimpleSynth()
{

}

void SimpleSynth::process()
{
  for (int i=0; i<256; i++) {
    switch (waveType) {
      case 0 : 
    }
    // buffer[i] = getSample()
    // osc.tick();
  }
}

void SimpleSynth::setWaveform()
{
  // set new wavetype
}
