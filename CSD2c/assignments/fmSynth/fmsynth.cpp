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
  car->setFrequency(this->frequency, samplerate);
  mod->setFrequency(this->frequency, samplerate);
}

void FMSynth::noteOn(float midi)
{
  std::cout << "(fmsynth) noteOn: " << midi << std::endl;
  this->midi = midi;
  setFrequency(mtof(this->midi));
}

void FMSynth::process(float *sampleBuf, int frames)
{
  for (int i=0; i<frames; i++)
  {
    sampleBuf[i] = mod->getSample();
    car->setFrequency(mtof(midi) + (sampleBuf[i] * fmIndex), samplerate);
    sampleBuf[i] = car->getSample() * gain;

    mod->tick();
    car->tick();
  }
}
