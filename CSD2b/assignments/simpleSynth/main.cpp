#include <cmath>
#include <iostream>
#include "simplesynth.h"
#include "oscillator.h"
#include "sinewave.h"
#include "squarewave.h"

float samples[256];

int main(int argc, char *argv[])
{
  SimpleSynth testSynth;
  testSynth.setGain(1);
  testSynth.process(samples);

  // Print the audio
  for (int i=0; i<256; i++) {
    std::cout << samples[i] << std::endl;
  }

  testSynth.setWave(1);

  

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
