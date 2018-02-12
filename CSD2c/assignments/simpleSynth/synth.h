#ifndef _SYNTH_H_
#define _SYNTH_H_

class Synth
{
public:
  Synth(float sampleRate);
  ~Synth();
  void setGain(float gain);
protected:
  float frequency;
  float gain;
  float sampleRate;
};

#endif
