#ifndef _FMSYNTH_H_
#define _FMSYNTH_H_

#include "dsp/sinewave.h"
#include "synth.h"

class FMSynth : public Synth
{
public:
  FMSynth();
  virtual ~FMSynth();
  void setFrequency(float frequency);
  void noteOn(float midi);
  void process(float *sampleBuf, int frames);
private:
  Oscillator* carrier;
  Oscillator* modulator;
  SineWave sine1;
  SineWave sine2;
  float mod;
  float fmIndex = 100;
};

#endif
