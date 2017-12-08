#include "sinewave.h"
#include "squarewave.h"

#ifndef _SIMPLESYNTH_H_
#define _SIMPLESYNTH_H_

class SimpleSynth
{
public:
  SimpleSynth();
  virtual ~SimpleSynth(); // waarom moet deze virtual??? <<<<<<<<<<<
  void setGain(float gain);
  void setWave(int newWave);
  void process(float *outputBufferRef);
private:
  Oscillator* osc;
  SineWave sine;
  SquareWave sqr;
  float gain;
};

#endif
