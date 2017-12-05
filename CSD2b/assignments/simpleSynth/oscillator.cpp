#include <cmath>
#include <iostream>
#include "oscillator.h"

Oscillator::Oscillator()
{
  phase = 0;
  tickInc = 0;
}

Oscillator::~Oscillator()
{
}

void Oscillator::setFrequency(float hz, int sampleRate)
{
  /*
  CALCULATION FOR THE PHASE INCREMENT FOR A SINGLE TICK

  hz to seconds            1 / hz
  seconds to samples       (1 / hz) * sampleRate
  samples to phase incr    (2 * PI) / ((1 / hz) * sampleRate)

  the final calculation is:

         2 * pi
  --------------------
  (1/hz) * sampleRate

  which in C++ is:

  (2 * M_PI) / ((1 / hz) * sampleRate)

  */
  if (hz < 0.5 * sampleRate) {
    frequency = hz;
    tickInc = (2 * M_PI) / ((1 / hz) * sampleRate);
    std::cout << "Oscillator frequency set to " << hz << "hz @ " << sampleRate << ". Each tick will increment the phase by " << tickInc << std::endl;
  }
  else {
    std::cout << "! Oscillator frequency cannot be set above the nyquist frequency (" << 0.5 * sampleRate << "hz)" << std::endl;
  }
}

void Oscillator::tick()
{
  phase += tickInc;
}
