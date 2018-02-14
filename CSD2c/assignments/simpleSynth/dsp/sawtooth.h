#ifndef _SAWTOOTH_H_
#define _SAWTOOTH_H_

#include "oscillator.h"

class Sawtooth : public Oscillator
{
public:
  Sawtooth();
  ~Sawtooth();
  double getSample();
protected:
};

#endif
