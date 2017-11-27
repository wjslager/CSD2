#ifndef _VIERKANT_H_
#define _VIERKANT_H_

#include "figuur.h"

class Vierkant : public Figuur
{
public:
  Vierkant(int x, int y);
  ~Vierkant();

  void teken();
private:
  int breedte, hoogte;
};

#endif

// De x en y zijn private van Figuur
// Die kun je dus bereiken door ze protected te maken of
// door een functie te maken zoals setX
