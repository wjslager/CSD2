#include <iostream>
#include "figuur.h"

Figuur::Figuur(int x, int y)
{
  std::cout << "Figuurtje geschept op " << x << ", " << y << std::endl;
  this->x = x; // this->x slaat op de x van de class zelf, de andere x is de variabele
  this->y = y;
}

Figuur::~Figuur()
{
  std::cout << "Figuurtje vernietigd" << std::endl;
}

void Figuur::teken()
{
  std::cout << "Figuurtje getekent op positie " << x << ", " << y << std::endl;
}

void Figuur::verplaats(int x, int y)
{
  this->x = x;
  this->y = y;
  std::cout << "Figuurtje verplaatst naar de positie " << x << ", " << y << std::endl;
}

void Figuur::wijzigSnelheid(int snelheid)
{
  this->snelheid = snelheid;
}
