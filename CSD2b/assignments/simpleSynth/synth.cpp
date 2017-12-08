#include <iostream>
#include "synth.h"

Synth::Synth(float sampleRate)
{
  std::cout << "Synth constructor" << std::endl;
  this->sampleRate = sampleRate;
}

Synth::~Synth()
{
  std::cout << "Synth deconstructor" << std::endl;
}

void Synth::setGain(float gain)
{
  this->gain = gain;
}
