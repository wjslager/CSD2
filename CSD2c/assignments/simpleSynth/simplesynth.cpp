#include <iostream>
#include "synth.h"
#include "simplesynth.h"
#include "dsp/oscillator.h"
#include "dsp/sinewave.h"
#include "dsp/squarewave.h"

SimpleSynth::SimpleSynth() : Synth()
{
  // Defaults to sinewave with a gain of 1
  osc = &sine;
  gain = 1;
}

SimpleSynth::~SimpleSynth()
{}

void SimpleSynth::setFrequency(float newFrequency, int newSamplerate)
{
  frequency = newFrequency;
  sampleRate = newSamplerate;
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

void SimpleSynth::process(float *outputBufferRef, int frames)
{
  for (int i=0; i<frames; i++) {
    outputBufferRef[i] = osc->getSample() * gain;
    osc->tick();
  }
}
