#ifndef _INSTRUMENT_H_
#define _INSTRUMENT_H_

class Instrument
{
public:
  Instrument(std::string sound);
  void setSound(std::string sound);
  void play(std::string articulation);
private:
  std::string sound;
};

#endif
