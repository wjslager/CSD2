#include <cmath>
#include <iostream>
#include "squarewave.h"

SquareWave::SquareWave() : Oscillator()
{
}

SquareWave::~SquareWave()
{
}

double SquareWave::getSample()
{
  // If (phase < PI) return 1, else -1
  return phase < M_PI ? 1 : -1;
}
