#ifndef _SQUAREWAVE_H_
#define _SQUAREWAVE_H_

class SquareWave
{
public:
  SquareWave();
  ~SquareWave();
  void getSample(double phase);
private:
  double sample;
};

#endif
