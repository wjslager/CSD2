#ifndef _SIMPLESYNTH_H_
#define _SIMPLESYNTH_H_

#include "dsp/sinewave.h"
#include "dsp/squarewave.h"
#include "synth.h"

class SimpleSynth : public Synth
{
public:
  SimpleSynth(float sampleRate);
  virtual ~SimpleSynth(); // waarom moet deze virtual??? <<<<<<<<<<<
  void setFrequency(float newFrequency);
  void setWave(int newWave);
  void process(float *outputBufferRef);
private:
  Oscillator* osc;
  SineWave sine;
  SquareWave sqr;
};

#endif
