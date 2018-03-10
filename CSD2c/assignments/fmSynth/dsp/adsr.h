#ifndef _ADSR_H_
#define _ADSR_H_

#include "envelope.h"

class ADSR : public Envelope
{
public:
  ADSR();
  ~ADSR();
  void noteOn();
  void noteOff();
  double getSample();
protected:
  // the sample is raised to the power of the curve value
  // output = sample ^ curve
  float curve = 2;
  // time in samples
  float attack = 240;
  float decay = 96000;
  float release = 24000;
  // volume in gain factor
  float sustain = 0.5;
private:
  int stage = 0;
};

#endif
