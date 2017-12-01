#include <iostream>
#include "instrument.h"

Instrument::Instrument(std::string sound)
{
  this->sound=sound;
  std::cout << " > Instrument created: " << sound << std::endl;
}

void Instrument::setSound(std::string sound)
{
  this->sound=sound;
  std::cout << " > Instrument changed to: " << sound << std::endl;
}

void Instrument::play(std::string articulation)
{
  std::cout << sound << " " << articulation << std::endl;
}
