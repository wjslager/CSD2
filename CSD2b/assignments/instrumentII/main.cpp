#include <iostream>
#include "instrument.h"
#include "percussion.h"
#include "pitched.h"

int main(int argc, char *argv[])
{
  Percussion kick("bonka");
  Percussion snare("tzz");
  Pitched piano("pling", 30, 60);
  Pitched toeter("BWAAaPPpp", 40, 50);
  kick.flam(6);
  snare.note();
  kick.note();
  snare.note();
  // piano.changeArticulation("nooter");
  piano.note(40);
  piano.note(42);
  piano.note(43);
  snare.flam(4);
  piano.note(44);
  piano.changeArticulation("FFF");
  piano.note(45);
  toeter.note(45);
  piano.note(45);
  piano.changeArticulation("PPP");
  piano.note(20);
}
