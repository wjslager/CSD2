#include <iostream>
#include "synth.h"
#include "fmsynth.h"
#include "midi.h"
#include "dsp/oscillator.h"
#include "dsp/sinewave.h"

FMSynth::FMSynth() : Synth()
{
  // Set both the carrier and the oscillator to a sinewave
  car = &sine1;
  mod = &sine2;
  gain = 1;
}

FMSynth::~FMSynth()
{}

void FMSynth::setFrequency()
{
  setFrequency(frequency);
}

void FMSynth::setFrequency(float frequency)
{
  this->frequency = frequency;
  car->setFrequency(this->frequency * carRatio, samplerate);
  mod->setFrequency(this->frequency * modRatio, samplerate);
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
    // (base frequency * carrier ratio) + (modulator * fmIndex)
    car->setFrequency((frequency * carRatio) + (mod->getSample() * fmIndex), samplerate);
    sampleBuf[i] = car->getSample() * gain;

    mod->tick();
    car->tick();
  }
}
