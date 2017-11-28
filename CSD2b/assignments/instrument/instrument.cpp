// Instrument class implementation and functions
#include <iostream>
#include "instrument.h"

Instrument::Instrument(std::string newsound)
{
  std::cout << " > Instrument created" << std::endl;
  Instrument::changeSound(newsound);
}

Instrument::~Instrument()
{
  std::cout << " > Instrument sold at local second-hand shop: " << sound << std::endl;
}

void Instrument::changeSound(std::string newsound)
{
  sound=newsound;
  std::cout << " > Instrument changed to: " << sound << std::endl;
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
