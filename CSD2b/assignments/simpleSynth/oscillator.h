#ifndef _OSCILLATOR_H_
#define _OSCILLATOR_H_

class Oscillator
{
public:
  Oscillator();
  ~Oscillator();
  void setFrequency(float hz, int sampleRate); //
  void tick();
protected:
  double phase;
private:
  double frequency; // in hz
  double tickInc; // value to add to phase for each tick
};

#endif

// M_PI
