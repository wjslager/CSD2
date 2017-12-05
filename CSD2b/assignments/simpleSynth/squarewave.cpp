#include <cmath>
#include <iostream>
#include "squarewave.h"

SquareWave::SquareWave() : Oscillator()
{
  sample = 0;
}

SquareWave::~SquareWave()
{

}

double SquareWave::getSample()
{
  sample = phase < M_PI ? 1 : -1;
  return sample;
}
