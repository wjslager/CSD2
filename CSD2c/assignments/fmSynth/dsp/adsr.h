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
  // Automatable values
  float curve = 2;
  float attack = 240;
  float decay = 96000;
  float sustain = 0.5;
  float release = 24000;
private:
  float preAttack = 32;
  int stage = 0;
};

#endif
