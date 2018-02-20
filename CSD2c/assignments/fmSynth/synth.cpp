#include <iostream>
#include "synth.h"

Synth::Synth()
{
  // std::cout << "Synth constructor" << std::endl;
}

Synth::Synth(float samplerate)
{
  // std::cout << "Synth constructor with samplerate" << std::endl;
  setSamplerate(samplerate);
}

Synth::~Synth()
{
  // std::cout << "Synth deconstructor" << std::endl;
}

void Synth::setGain(float gain)
{
  this->gain = gain;
}

void Synth::setSamplerate(float samplerate)
{
  this->samplerate = samplerate;
  std::cout << "(synth) Setting samplerate to " << samplerate << std::endl;
}
