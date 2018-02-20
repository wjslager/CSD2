#include <iostream>
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
  // Skip to the release stage
  phase = 1;
  stage = 3;
  // std::cout << "(adsr) note off" << std::endl;
}

double ADSR::getSample()
{
  if (phase >= 1) {
    // phase >= 1 when a line ends
    switch(stage) {
      case 0:
        // ATTACK stage
        line(0, 1, attack);
        stage++;
        break;
      case 1:
        // DECAY stage
        line(1, sustain, decay);
        stage++;
        break;
      case 2:
        // SUSTAIN STAGE
        break;
      case 3:
        // RELEASE stage
        line(value, 0, release);
        stage++;
        break;
    }
  }
  return value;
}
