#include <iostream>
#include "instrument.h"

Instrument::Instrument(std::string sound)
{
  std::cout << " > Instrument created" << std::endl;
  Instrument::changeSound(sound);
}

void Instrument::changeSound(std::string sound)
{
  this->sound = sound;
  std::cout << " > Instrument sound changed to: " << sound << std::endl;
}

void Instrument::play(std::string articulation)
{
  std::cout << sound << " " << articulation << std::endl;
}
