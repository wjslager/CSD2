#ifndef _OSCILLATOR_H_
#define _OSCILLATOR_H_

class Oscillator
{
public:
  Oscillator();
  ~Oscillator();
  void setFrequency(float hz, int sampleRate);
  void tick();
protected:
  float phase;
private:
  float tickInc; // value to add to phase for each tick
  float frequency; // in hz
};

#endif
