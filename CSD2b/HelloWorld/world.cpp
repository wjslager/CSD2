#include <iostream>
#include "world.h"

World::World(int newyear)
{
  year=newyear;
}

void World::setyear(int newyear)
{
  year=newyear;
}

void World::hallo()
{
  std::cout << "Hallo mag ik een frietje in het jaar " << year << std::endl;
}
