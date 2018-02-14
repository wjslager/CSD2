#include <iostream>
#include "phasor.h"
#include "oscillator.h"

Phasor::Phasor() : Oscillator()
{
  // std::cout << "Phasor constructor" << std::endl;
}

Phasor::~Phasor()
{
  // std::cout << "Phasor deconstructor" << std::endl;
}

double Phasor::getSample()
{
  return phase / PI_2;
}
