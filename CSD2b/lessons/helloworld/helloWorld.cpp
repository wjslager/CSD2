#include <iostream>
#include "world.h"

int main()
{
  World wereld(2000);

  wereld.hallo();
  wereld.setyear(2001);
  wereld.hallo();
  return 0;
}
