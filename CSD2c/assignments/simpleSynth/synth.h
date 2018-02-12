#ifndef _SYNTH_H_
#define _SYNTH_H_

class Synth
{
public:
  Synth();
  ~Synth();
  void setGain(float gain);
protected:
  float frequency;
  float gain;
  float sampleRate;
};

#endif
