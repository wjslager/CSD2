#ifndef _SIMPLESYNTH_H_
#define _SIMPLESYNTH_H_

#include "dsp/sinewave.h"
#include "dsp/squarewave.h"
#include "synth.h"

class SimpleSynth : public Synth
{
public:
  SimpleSynth();
  virtual ~SimpleSynth();
  void setFrequency(float newFrequency, int newSamplerate);
  void setWave(int newWave);
  void process(float *outputBufferRef, int frames);
private:
  Oscillator* osc;
  SineWave sine;
  SquareWave sqr;
};

#endif
