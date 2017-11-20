#include <iostream>
#include "instrument.h"

Instrument::Instrument(std::string newsound)
{
  sound=newsound;
}

void Instrument::changeSound(std::string newsound)
{
  sound=newsound;
}

// Play the sound
void Instrument::makeSound()
{
  std::cout << sound << std::endl;
}

// Play the sound multiple times
void Instrument::uziSound(int clipsize)
{
  for (int i=0; i<clipsize; i++) makeSound();
}

// Instrument class implementation
