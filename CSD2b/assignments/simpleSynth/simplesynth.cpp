#include <iostream>
#include "synth.h"
#include "simplesynth.h"
#include "oscillator.h"
#include "sinewave.h"
#include "squarewave.h"

SimpleSynth::SimpleSynth(float sampleRate) : Synth(sampleRate)
{
  // Defaults to sinewave with a gain of 1
  osc = &sine;
  gain = 1;
  osc->setFrequency(20, sampleRate);
}

SimpleSynth::~SimpleSynth()
{
  // std::cout << "Simplesynth deconstructor" << std::endl;
}

void SimpleSynth::setFrequency(float newFrequency)
{
  frequency = newFrequency;
  osc->setFrequency(frequency, sampleRate);
}

void SimpleSynth::setWave(int newWave)
{
  switch (newWave) {
    case 0 :
      osc = &sine;
      osc->setFrequency(20, 48000);
      break;
    case 1 :
      osc = &sqr;
      osc->setFrequency(20, 48000);
      break;
    default :
      std::cout << "setWave choice not valid" << std::endl;
  }
}


void SimpleSynth::process(float *outputBufferRef)
{
  for (int i=0; i<256; i++) {
    outputBufferRef[i] = osc->getSample() * gain;
    osc->tick();
  }
}
