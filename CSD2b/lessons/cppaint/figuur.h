#ifndef _FIGUUR_H_
#define _FIGUUR_H_

#include <iostream>

class Figuur
{
public:
  Figuur(int x, int y);
  ~Figuur(); // destructor

  void teken();
  void verplaats(int x, int y);
  void wijzigSnelheid(int snelheid);
private:
  int x, y;
  int snelheid;
};

#endif
// Alternatief
// #pragma once

// constructor en destructor hebben geen return type omdat ze het object teruggeven.
// Verschillende constructors kunnen bestaan welke worden gekozen gebaseerd
// op welke argumenten zijn meegegeven.

// destructor
// aangeroepen als een object wordt opgeruimd
// Als je binnen een functie een object aanmaakt wordt deze opgeruimd
// zodra de functie voorbij is.
// destructors zijn handig om dingen zoals files schrijven af te maken

// Memory leak is als je een boel objecten maakt zonder dat je deze kan weghalen later
