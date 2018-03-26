#ifndef _SAMPLEDELAY_H_
#define _SAMPLEDELAY_H_

class SampleDelay
{
public:
  SampleDelay(unsigned long delayLength);
  ~SampleDelay();
  void write(double sample);
  double read(unsigned long offset);
  void tick();
private:
  double* buffer;
  unsigned long delayLength;
  unsigned long writeIndex = 0;
};

#endif
