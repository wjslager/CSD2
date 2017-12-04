#include <cmath>
#include <iostream>
#include "sinewave.h"

SineWave::SineWave()
{
  sample = 0;
}

SineWave::~SineWave()
{

}

void SineWave::getSample(double phase)
{
  sample = sin(phase);
  std::cout << sample << std::endl;
}
