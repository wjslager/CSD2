#ifndef _SIMPLESYNTH_H_
#define _SIMPLESYNTH_H_

#include "dsp/sinewave.h"
#include "dsp/squarewave.h"
#include "dsp/sawtooth.h"
#include "dsp/phasor.h"
#include "synth.h"

class SimpleSynth : public Synth
{
public:
  SimpleSynth();
  virtual ~SimpleSynth();
  void setFrequency(float frequency);
  void setWave(int waveform);
  void process(float *sampleBuf, int frames);
private:
  Oscillator* osc;
  SineWave sine;
  SquareWave sqr;
  Sawtooth saw;
};

#endif
