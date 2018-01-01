#include <cmath>
#include <iostream>
#include "synth.h"
#include "simplesynth.h"
#include "oscillator.h"
#include "sinewave.h"
#include "squarewave.h"

float samples[256];

int main(int argc, char *argv[])
{
  SimpleSynth test(48000);
  test.setGain(1);
  test.setFrequency(2000);
  test.process(samples);

  // Print the audio
  for (int i=0; i<256; i++) {
    std::cout << samples[i] << std::endl;
  }

  test.setWave(1);
  test.setFrequency(24500); // is above the nyquist so it will not change the frequency
  test.setFrequency(8000);
  test.setGain(0.5);
  test.process(samples);

  // Print the audio
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

  // std::cout << "lattteerrr" << std::endl;
  return 0;
}
