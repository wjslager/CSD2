#ifndef _OSCILLATOR_H_
#define _OSCILLATOR_H_

#define PI_2 6.28318530717959
#define PI 3.141592653589795

class Oscillator
{
public:
  Oscillator();
  ~Oscillator();
  void setFrequency(float hz, int sampleRate);
  void tick();
  virtual double getSample() = 0;
protected:
  float phase;
  float frequency; // in hz
private:
  float phaseInc; // value to add to phase for each tick
};

#endif
