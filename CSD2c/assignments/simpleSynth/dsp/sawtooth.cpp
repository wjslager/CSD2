#include <cmath>
#include <iostream>
#include "sawtooth.h"
#include "oscillator.h"

Sawtooth::Sawtooth() : Oscillator()
{
  // std::cout << "Sinewave constructor" << std::endl;
}

Sawtooth::~Sawtooth()
{
  // std::cout << "Sinewave deconstructor" << std::endl;
}

double Sawtooth::getSample()
{
  return phase / PI_2;
}
