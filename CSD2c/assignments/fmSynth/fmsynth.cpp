#include <iostream>
#include "synth.h"
#include "fmsynth.h"
#include "midi.h"
#include "dsp/oscillator.h"
#include "dsp/sinewave.h"

FMSynth::FMSynth() : Synth()
{
  carrier = &sine1;
  modulator = &sine2;
  gain = 1;
}

FMSynth::~FMSynth()
{}

void FMSynth::setFrequency(float frequency)
{
  this->frequency = frequency;
  carrier->setFrequency(this->frequency, samplerate);
  modulator->setFrequency(this->frequency, samplerate);
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
    carrier->setFrequency(mtof(midi) + (modulator->getSample() * fmIndex), samplerate);
    sampleBuf[i] = carrier->getSample() * gain;

    modulator->tick();
    carrier->tick();
  }
}
