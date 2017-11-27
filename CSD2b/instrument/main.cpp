#include <iostream>
#include "instrument.h"

int main(int argc, char *argv[])
{
  Instrument kick("boom");
  Instrument snare("plok");

  // Replace default sounds with arguments specified at boot
  if (argc > 2) {
    kick.changeSound(argv[1]);
    snare.changeSound(argv[2]);
  } else {
    std::cout << " ! No arguments specified, using default sounds" << std::endl;
  }

  kick.makeSound();
  kick.makeSound();
  snare.makeSound();
  snare.changeSound("kra");
  snare.makeSound();
  snare.changeSound("ka");
  snare.uziSound(2);
  kick.changeSound("BOOM");
  kick.uziSound(10);
}
