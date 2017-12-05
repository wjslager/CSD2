#include <cmath>
#include <iostream>
#include "oscillator.h"
#include "sinewave.h"
#include "squarewave.h"

int main(int argc, char *argv[])
{
  // Declare oscillators
  SineWave sine;
  SquareWave sqr;
  sine.setFrequency(200, 48000);
  std::cout.precision(2);

  // Render some samples of a sinewave
  for (int i=0; i<20; i++) {
    std::cout << 1*sine.getSample() << std::endl;
    sine.tick();
  }

  // Render some samples of a sinewave
  for (int i=0; i<20; i++) {
    std::cout << sqr.getSample() << std::endl;
    sqr.tick();
  }
}
