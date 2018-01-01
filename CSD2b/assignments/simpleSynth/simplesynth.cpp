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
  // Point osc to the right class instance
  switch (newWave) {
    case 0 :
      osc = &sine;
      break;
    case 1 :
      osc = &sqr;
      break;
    default :
      std::cout << "setWave choice not valid" << std::endl;
  }

  // Reset the frequency after each change of wave
  // to make sure the current oscillator is up-to-date
  osc->setFrequency(frequency, sampleRate);
}


void SimpleSynth::process(float *outputBufferRef)
{
  // Calculate 256 samples and apply gain
  for (int i=0; i<256; i++) {
    outputBufferRef[i] = osc->getSample() * gain;
    osc->tick();
  }
}
