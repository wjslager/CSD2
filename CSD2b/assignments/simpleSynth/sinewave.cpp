#include <cmath>
#include "sinewave.h"

SineWave::SineWave() : Oscillator()
{
}

SineWave::~SineWave()
{
}

double SineWave::getSample()
{
  return sin(phase);
}
