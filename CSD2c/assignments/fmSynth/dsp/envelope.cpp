#include <cmath>
#include <iostream>
#include "envelope.h"

Envelope::Envelope()
{
  phase = 0;
  phaseInc = 0;
  // std::cout << "Envelope constructor" << std::endl;
}

Envelope::~Envelope()
{
  // std::cout << "Envelope deconstructor" << std::endl;
}

void Envelope::line(float start, float end, float frames)
{
  phase = 0;
  phaseInc = 1/frames;
  delta = end - start;
  this->start = start;
}

double Envelope::getSample()
{
  return value;
}

void Envelope::tick()
{
  if (phase < 1) {
    value = (delta * phase) + start;
    phase += phaseInc;
  }
}
