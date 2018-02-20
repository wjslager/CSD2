#ifndef _FMSYNTH_H_
#define _FMSYNTH_H_

#include "dsp/sinewave.h"
#include "synth.h"

class FMSynth : public Synth
{
public:
  FMSynth();
  virtual ~FMSynth();
  void setFrequency();
  void setFrequency(float frequency);
  void noteOn(float midi);
  void process(float *sampleBuf, int frames);

  /* Modifying the synthesizer parameters:
   *
   * fmSynth.fmIndex = 200;
   * fmSynth.carRatio = 2;
   * fmSynth.setFrequency;
   *
   * This makes sure the new values will go into effect immediately
   */
  float fmIndex = 1000;
  float carRatio = 1;
  float modRatio = 1;
private:
  Oscillator* car;
  SineWave sine1;
  Oscillator* mod;
  SineWave sine2;
};

#endif
