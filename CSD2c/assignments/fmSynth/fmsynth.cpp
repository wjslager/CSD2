#include <iostream>
#include "synth.h"
#include "fmsynth.h"
#include "midi.h"
#include "dsp/oscillator.h"
#include "dsp/sinewave.h"

FMSynth::FMSynth() : Synth()
{
  car = &sine1;
  mod = &sine2;
  gain = 1;
}

FMSynth::~FMSynth()
{}

void FMSynth::setFrequency(float frequency)
{
  this->frequency = frequency;
  car->setFrequency(this->frequency * carRatio, samplerate);
  mod->setFrequency(this->frequency * modRatio, samplerate);
}

// Can be used to recalculate frequency values after changing carrier ratios
void FMSynth::setFrequency()
{
  setFrequency(frequency);
}

void FMSynth::noteOn(float midi)
{
  std::cout << "(fmsynth) noteOn: " << midi << std::endl;
  frequency = mtof(midi);
  setFrequency(frequency);
  // trigger envelopes here
}

void FMSynth::process(float *sampleBuf, int frames)
{
  for (int i=0; i<frames; i++)
  {
    sampleBuf[i] = mod->getSample();
    car->setFrequency((frequency * carRatio) + (sampleBuf[i] * fmIndex), samplerate);
    sampleBuf[i] = car->getSample() * gain;

    mod->tick();
    car->tick();
  }
}
