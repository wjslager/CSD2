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
  void setFrequency();
  void noteOn(float midi);
  void process(float *sampleBuf, int frames);

  float fmIndex = 1000;
  float carRatio = 1;
  float modRatio = 1;
protected:
private:
  Oscillator* car;
  Oscillator* mod;
  SineWave sine1;
  SineWave sine2;
};

#endif
