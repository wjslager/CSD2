#include <iostream>
#include <cmath>
#include "adsr.h"

ADSR::ADSR()
{
  // std::cout << "ADSR constructor" << std::endl;
}

ADSR::~ADSR()
{
  // std::cout << "ADSR destructor" << std::endl;
}

void ADSR::noteOn()
{
  phase = 1;
  stage = 0;
  // std::cout << "(adsr) note on" << std::endl;
}

void ADSR::noteOff()
{
  // Immediately go to the release stage
  phase = 1;
  stage = 4;
  // std::cout << "(adsr) note off" << std::endl;
}

double ADSR::getSample()
{
  // phase >= 1 is true when a line ends
  // thus the switch statement will only be evaluated at that point
  if (phase >= 1)
  {
    switch(stage)
    {
      case 0:
        // pre attack which slides from the current value to 0
        // used to ensure the envelope can retrigger while active without clicks
        line(value, 0, 32);
        stage++;
        break;
      case 1:
        /* === ATTACK === */
        line(0, 1, attack);
        stage++;
        break;
      case 2:
        /* === DECAY === */
        line(1, sustain, decay);
        stage++;
        break;
      case 3:
        /* ==== SUSTAIN === */
        // nothing happens when we reach 'sustain'
        // as it can only be ended by noteOff()
        break;
      case 4:
        /* === RELEASE === */
        line(value, 0, release);
        stage++;
        break;
    }
  }
  return pow(value, curve);
}
