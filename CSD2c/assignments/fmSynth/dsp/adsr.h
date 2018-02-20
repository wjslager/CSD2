#ifndef _ADSR_H_
#define _ADSR_H_

#include <iostream>
#include "envelope.h"

class ADSR : public Envelope
{
public:
  ADSR();
  ~ADSR();
  void noteOn();
  void noteOff();
private:
  float attack = 48000;
  float decay = 48000;
  float sustain = 0.1;
  float release = 48000;
};

#endif
