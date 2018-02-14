#include <cmath>
#include <iostream>
#include "attackdecay.h"

AttackDecay::AttackDecay()
{
  phase = 0;
  // std::cout << "AttackDecay constructor" << std::endl;
}

AttackDecay::~AttackDecay()
{
  // std::cout << "AttackDecay deconstructor" << std::endl;
}

void AttackDecay::setEnvelope(float hz, int sampleRate)
{
}

void AttackDecay::noteOn()
{
}

double AttackDecay::getSample()
{
}

void AttackDecay::tick()
{
  phase++;
}
