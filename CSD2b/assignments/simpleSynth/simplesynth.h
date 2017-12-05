#include "sinewave.h"

#ifndef _SIMPLESYNTH_H_
#define _SIMPLESYNTH_H_

class SimpleSynth
{
public:
  // enum waveType{sine, square};

  SimpleSynth();
  ~SimpleSynth();
  void process(float *outputBufferRef);
private:
  SineWave oscillator;
};

#endif
