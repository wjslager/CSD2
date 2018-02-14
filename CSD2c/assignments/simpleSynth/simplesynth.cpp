#include <iostream>
#include "synth.h"
#include "simplesynth.h"
#include "dsp/oscillator.h"
#include "dsp/sinewave.h"
#include "dsp/squarewave.h"
#include "dsp/sawtooth.h"

SimpleSynth::SimpleSynth() : Synth()
{
  // Defaults to sinewave with a gain of 1
  osc = &sine;
  gain = 1;
}

SimpleSynth::~SimpleSynth()
{}

void SimpleSynth::setFrequency(float frequency)
{
  this->frequency = frequency;
  osc->setFrequency(this->frequency, samplerate);
}

void SimpleSynth::setWave(int waveform)
{
  // Point osc to the right class instance
  switch (waveform) {
    case 0 :
      osc = &sine;
      break;
    case 1 :
      osc = &sqr;
      break;
    case 2 :
      osc = &saw;
      break;
    default :
      std::cout << "(simplesynth) setWave choice not valid" << std::endl;
      return;
  }
  std::cout << "(simplesynth) setWave to " << waveform << ". Will now call setFrequency to be sure" << std::endl;

  // Reset the frequency after each change of wave
  // to make sure the current oscillator is up-to-date
  osc->setFrequency(frequency, samplerate);
}

void SimpleSynth::process(float *sampleBuf, int frames)
{
  for (int i=0; i<frames; i++)
  {
    sampleBuf[i] = osc->getSample() * gain;
    osc->tick();
  }
}
