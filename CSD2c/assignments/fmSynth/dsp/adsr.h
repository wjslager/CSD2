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
private:
  bool note = false;
  int stage = 0; // tracks which envelope segment we are in
  float attack = 4800;
  float decay = 48000;
  float sustain = 0.1;
  float release = 480;
};

#endif
