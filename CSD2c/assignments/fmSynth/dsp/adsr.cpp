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
  // ATTACK stage
  line(0, 1, attack);
  std::cout << "attack" << std::endl;

  // DECAY stage
  line(1, sustain, decay);
  std::cout << "decay" << std::endl;

  // SUSTAIN stage
  // Do nothing until the release stage is triggered
  std::cout << "sustain" << std::endl;
}

void ADSR::noteOff()
{
  // RELEASE stage
  line(sustain, 0, release);
  std::cout << "release" << std::endl;
}
