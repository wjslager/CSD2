#include <iostream>
#include "instrument.h"
#include "percussion.h"

Percussion::Percussion(std::string sound) : Instrument(sound)
{
  std::cout << " --> Type: Percussion" << std::endl << std::endl;
}

void Percussion::note()
{
  Instrument::play("");
}

void Percussion::flam(int length)
{
  for (int i=0; i<length; i++) {
    Instrument::play("(flam)");
  }
}
