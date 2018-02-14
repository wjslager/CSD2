#include <iostream>
#include "sawtooth.h"
#include "oscillator.h"

Sawtooth::Sawtooth() : Oscillator()
{
  // std::cout << "Sawtooth constructor" << std::endl;
}

Sawtooth::~Sawtooth()
{
  // std::cout << "Sawtooth deconstructor" << std::endl;
}

double Sawtooth::getSample()
{
  return -2 * (phase / PI_2) + 1;
}
