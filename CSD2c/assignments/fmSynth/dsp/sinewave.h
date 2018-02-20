#ifndef _SINEWAVE_H_
#define _SINEWAVE_H_

#include "oscillator.h"

class SineWave : public Oscillator
{
public:
  SineWave();
  ~SineWave();
  void tick();
  double getSample();
};

#endif
