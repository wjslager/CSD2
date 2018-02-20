#include <iostream>
#include "fmsynth.h"
#include "midi.h"

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
  // Store the frequency and pass it to the oscillators
  frequency = mtof(midi);
  setFrequency(frequency);

  // Trigger all envelopes
  carEnv.noteOn();
  modEnv.noteOn();
}

void FMSynth::noteOff()
{

}

void FMSynth::process(float *sampleBuf, int frames)
{
  for (int i=0; i<frames; i++)
  {
    // (base frequency * carrier ratio) + (modulator * fmIndex)
    car->setFrequency((frequency * carRatio) + (mod->getSample() * fmIndex * modEnv.getSample()), samplerate);
    sampleBuf[i] = car->getSample() * gain * carEnv.getSample();

    mod->tick();
    car->tick();
    carEnv.tick();
    modEnv.tick();
  }
}
