#include <cmath>
#include <iostream>
#include "oscillator.h"

Oscillator::Oscillator()
{
  phase = 0;
  tickInc = 0.1;
}

Oscillator::~Oscillator()
{

}

void Oscillator::setFrequency(float hz, int sampleRate)
{
  frequency = hz;
  tickInc = (2 * M_PI) / ((1 / hz) * sampleRate);

  /* CALCULATION THE PHASE INCREMENT FOR A SINGLE TICK
  hz to seconds            1 / hz
  seconds to samples       (1 / hz) * sampleRate
  samples to phase incr    (2 * PI) / ((1 / hz) * sampleRate)

         2 * pi
  --------------------
  (1/hz) * sampleRate

  */
  std::cout << "osc:frequency set to " << hz << "hz @ " << sampleRate << ". Each tick will increment the phase by " << tickInc << std::endl;
}

void Oscillator::tick()
{
  // std::cout << "tick" << std::endl;
  phase += tickInc;
}
