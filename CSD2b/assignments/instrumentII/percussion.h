#ifndef _PERCUSSION_H_
#define _PERCUSSION_H_

class Percussion : public Instrument
{
public:
  Percussion(std::string sound);
  void note();
  void flam(int length);
};

#endif
