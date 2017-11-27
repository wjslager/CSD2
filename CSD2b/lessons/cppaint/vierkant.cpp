#include "vierkant.h"

Vierkant::Vierkant(int x, int y) : Figuur(x, y)
{
  std::cout << "Vierkantje geschept" << std::endl;
}

Vierkant::~Vierkant()
{
  std::cout << "Vierkantje vernietigd" << std::endl;
}

void Vierkant::teken()
{
  std::cout << "Vierkantje getekent" << std::endl;
}
