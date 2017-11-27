#include <iostream>
#include "instrument.h"

int main(int argc, char *argv[])
{
  // Create instruments using the default sounds
  Instrument kick("boom");
  Instrument snare("plok");

  // Replace default sounds with arguments specified at boot (if specified)
  if (argc > 2) {
    kick.changeSound(argv[1]);
    snare.changeSound(argv[2]);
  } else {
    std::cout << " ! Not enough arguments specified, using default sounds" << std::endl;
  }

  // Play some sounds
  kick.makeSound();
  kick.makeSound();
  snare.makeSound();
  // KRA-KA-KA
  snare.changeSound("kra");
  snare.makeSound();
  snare.changeSound("ka");
  snare.uziSound(2);
  // BOOM BOOM BOOM BOOM BOOM
  kick.changeSound("BOOM");
  kick.uziSound(5);
}
