#ifndef _PITCHED_H_
#define _PITCHED_H_

class Pitched : public Instrument
{
public:
  Pitched(std::string sound, int minPitch, int maxPitch);
  void changeArticulation(std::string articulation);
  void note(int pitch);
private:
  std::string articulation = "";
  int minPitch;
  int maxPitch;
};

#endif
