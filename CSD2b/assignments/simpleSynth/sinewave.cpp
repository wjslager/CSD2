#include <cmath>
#include "sinewave.h"

SineWave::SineWave() : Oscillator()
{
  sample = 0;
}

SineWave::~SineWave()
{

}

double SineWave::getSample()
{
  sample = sin(phase);
  return sample;
}
