#ifndef _ENVELOPE_H_
#define _ENVELOPE_H_

class Envelope
{
public:
  Envelope();
  ~Envelope();
  void tick();
  void line(float start, float end, float frames);
  double getSample();
protected:
  double value;
private:
  float phase;
  float phaseInc;
  float delta; // difference between start and end
  float start = 0;
};

#endif
