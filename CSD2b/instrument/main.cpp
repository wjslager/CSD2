#include <iostream>
#include "instrument.h"

int main()
{
  Instrument kick("BOEM");
  Instrument snare("KLAP");

  kick.makeSound();
  kick.changeSound("BONG");
  kick.makeSound();
  snare.makeSound();
  snare.changeSound("PLOK");
  snare.uziSound(4);
}
