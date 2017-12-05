#ifndef _SQUAREWAVE_H_
#define _SQUAREWAVE_H_

#include "oscillator.h"

class SquareWave : public Oscillator
{
public:
  SquareWave();
  ~SquareWave();
  double getSample();
private:
  double sample;
};

#endif
