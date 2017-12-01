#include <iostream>
#include "instrument.h"
#include "pitched.h"

Pitched::Pitched(std::string sound, int minPitch, int maxPitch) : Instrument(sound)
{
  this->minPitch = minPitch;
  this->maxPitch = maxPitch;
  std::cout << " --> Type: Pitched. Range: " << minPitch << " to " << maxPitch << std::endl;
}

void Pitched::changeArticulation(std::string articulation)
{
  this->articulation = articulation;
  std::cout << " > Articulation has been changed to " << articulation << std::endl;
}

void Pitched::note(int pitch)
{
  if (pitch >= minPitch && pitch <= maxPitch) {
    Instrument::play(std::to_string(pitch) + " " + articulation);
  }
  else {
    std::cout << " ! " << pitch << " is out of range for this instrument" << std::endl;
  }

}
