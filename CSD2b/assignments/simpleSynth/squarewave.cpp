#include <cmath>
#include <iostream>
#include "squarewave.h"

SquareWave::SquareWave()
{
  sample = 0;
}

SquareWave::~SquareWave()
{

}

void SquareWave::getSample(double phase)
{
  sample = phase < M_PI ? 1 : -1;
  std::cout << sample << std::endl;
}
