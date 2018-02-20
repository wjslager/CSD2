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
  // Skip to the release stage
  phase = 1;
  stage = 4;
  // std::cout << "(adsr) note off" << std::endl;
}

double ADSR::getSample()
{
  if (phase >= 1) {
    // phase >= 1 when a line ends
    switch(stage) {
      case 0:
        // pre attack which slides from the current value to 0
        // used to ensure the envelope can retrigger without clicks
        line(value, 0, preAttack);
        stage++;
        break;
      case 1:
        // === ATTACK
        line(0, 1, attack);
        stage++;
        break;
      case 2:
        // === DECAY
        line(1, sustain, decay);
        stage++;
        break;
      case 3:
        // ==== SUSTAIN
        // value will be left at 'sustain'
        // the next stage will be triggered by noteOff()
        break;
      case 4:
        // === RELEASE
        line(value, 0, release);
        stage++;
        break;
    }
  }
  return pow(value, curve);
}
