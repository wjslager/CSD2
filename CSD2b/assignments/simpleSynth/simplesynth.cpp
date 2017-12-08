#include <iostream>
#include "simplesynth.h"
#include "oscillator.h"
#include "sinewave.h"
#include "squarewave.h"

SimpleSynth::SimpleSynth()
{
  // Defaults to sinewave with a gain of 1
  osc = &sine;
  gain = 1;
  osc->setFrequency(20, 48000);
}

SimpleSynth::~SimpleSynth()
{
  // std::cout << "Simplesynth deconstructor" << std::endl;
}

void SimpleSynth::setGain(float gain)
{
  this->gain = gain;
}

void SimpleSynth::setWave(int newWave)
{
  switch (newWave) {
    case 0 :
      osc = &sine;
      break;       // and exits the
    case 1 :
      osc = &sqr;
      break;
  }
}


void SimpleSynth::process(float *outputBufferRef)
{
  for (int i=0; i<256; i++) {
    outputBufferRef[i] = osc->getSample() * gain;
    osc->tick();
  }
}
