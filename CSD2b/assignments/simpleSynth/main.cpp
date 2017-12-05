#include <cmath>
#include <iostream>
#include "simplesynth.h"
#include "oscillator.h"
#include "sinewave.h"
#include "squarewave.h"

float samples[256];

int main(int argc, char *argv[])
{
  SimpleSynth testSine;

  testSine.process(samples);

  for (int i=0; i<256; i++) {
    std::cout << samples[i] << std::endl;
  }

  /*
  // Declare oscillators
  SineWave sine;
  SquareWave sqr;
  sine.setFrequency(200, 48000);

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
  */
}
