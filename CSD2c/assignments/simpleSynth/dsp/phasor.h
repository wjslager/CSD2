#ifndef _PHASOR_H_
#define _PHASOR_H_

#include "oscillator.h"

class Phasor : public Oscillator
{
public:
  Phasor();
  ~Phasor();
  double getSample();
protected:
};

#endif
