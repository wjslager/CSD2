#include <cmath>
#include <iostream>
#include "oscillator.h"

Oscillator::Oscillator()
{
  phase = 0;
  phaseInc = 0;
  // std::cout << "Oscillator constructor" << std::endl;
}

Oscillator::~Oscillator()
{
  // std::cout << "Oscillator deconstructor" << std::endl;
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

  frequency = hz;
  phaseInc = PI_2 / ((1 / hz) * sampleRate);
  // std::cout << "(osc) Frequency set to " << hz << "hz @ " << sampleRate << ". Tick set to " << phaseInc << std::endl;
}

void Oscillator::tick()
{
  // fmod is % for floats and doubles
  // wraps the phase around at twoPi to make sure the squarewave works
  // for more than one cycle
  phase = fmod((phase + phaseInc), PI_2);
}
