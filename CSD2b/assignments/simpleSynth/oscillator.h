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
  double phase;
private:
  double tickInc; // value to add to phase for each tick
  double frequency; // in hz
};

#endif
