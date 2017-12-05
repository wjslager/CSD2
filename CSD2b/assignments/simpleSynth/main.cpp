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

  sine.setFrequency(2, 48000);

  // Render a sinewave
  // for (int i=0; i<32; i++) {
  //   std::cout << sine.getSample() << std::endl;
  //   sine.tick();
  // }
}
