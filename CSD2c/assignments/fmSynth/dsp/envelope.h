#ifndef _ENVELOPE_H_
#define _ENVELOPE_H_

class Envelope
{
public:
  Envelope();
  ~Envelope();
  void setSamplerate(float samplerate);
  void line(float start, float end, float frames);
  void tick();

  virtual double getSample() = 0;
  virtual void noteOn() = 0;
  virtual void noteOff() = 0;
protected:
  double value;
  float samplerate;
  float phase;
private:
  float phaseInc;
  float delta; // difference between start and end
  float start = 0;
};

#endif
