#ifndef _SYNTH_H_
#define _SYNTH_H_

class Synth
{
public:
  Synth();
  ~Synth();
  void setGain(float gain);
  void setSamplerate(float samplerate);
protected:
  float frequency;
  float gain;
  float samplerate;
};

#endif
