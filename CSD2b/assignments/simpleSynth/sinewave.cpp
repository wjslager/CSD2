#include <cmath>
#include <iostream>
#include "sinewave.h"

SineWave::SineWave() : Oscillator()
{
  // std::cout << "Sinewave constructor" << std::endl;
}

SineWave::~SineWave()
{
  // std::cout << "Sinewave deconstructor" << std::endl;
}

double SineWave::getSample()
{
  return sin(phase);
}
