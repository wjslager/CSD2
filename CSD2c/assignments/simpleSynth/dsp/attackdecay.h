#ifndef _ATTACKDECAY_H_
#define _ATTACKDECAY_H_

class AttackDecay
{
public:
  AttackDecay();
  ~AttackDecay();
  void setEnvelope(float decay, int sampleRate); // modify envelope parameters
  void noteOn();
  // void noteOff();
  void tick();
  double getSample();
protected:
  // In this case, phase is counted in samples
  float phase;
private:
  float decay;
};

#endif
