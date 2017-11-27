#include "figuur.h"
#include "vierkant.h"

int main()
{
  Figuur cirkel(25, 47);
  Vierkant square(10, 20);
  square.teken();
  square.verplaats(20, 30);

  return 0;
}
