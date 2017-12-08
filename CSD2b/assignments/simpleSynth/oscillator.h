#ifndef _OSCILLATOR_H_
#define _OSCILLATOR_H_
#include <cmath>

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
  static constexpr double twoPi = 2 * M_PI;
private:
  float tickInc; // value to add to phase for each tick
  float frequency; // in hz
  // Static: shared by all instances
  // Constexpr: value calculated at compilation and thus not changeable
};

#endif
