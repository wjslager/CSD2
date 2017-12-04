#ifndef _SINEWAVE_H_
#define _SINEWAVE_H_

class SineWave
{
public:
  SineWave();
  ~SineWave();
  void getSample(double phase);
private:
  double sample;
};

#endif
