#include <cmath>
#include <iostream>
#include "squarewave.h"

SquareWave::SquareWave() : Oscillator()
{
  // std::cout << "Squarewave constructor" << std::endl;
}

SquareWave::~SquareWave()
{
  // std::cout << "Squarewave deconstructor" << std::endl;
}

double SquareWave::getSample()
{
  // If (phase < PI) return 1, else -1
  return phase < M_PI ? 1 : -1;
}
