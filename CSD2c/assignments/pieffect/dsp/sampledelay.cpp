#include "sampledelay.h"
#include "../wmath.h" // provides a mathematically correct modulo

SampleDelay::SampleDelay(unsigned long delayLength)
{
  // Store the buffersize, then initialize the buffer
  this->delayLength = delayLength;
  buffer = new double[delayLength];
  for (unsigned long i = 0; i < this->delayLength; i++)
  {
    buffer[i] = 0;
  }
}

SampleDelay::~SampleDelay()
{
  // Delete the buffer and make it a nullpointer just to be sure
  delete[] buffer;
  buffer = nullptr;
}

void SampleDelay::write(double sample)
{
  buffer[writeIndex] = sample;
  tick();
}

double SampleDelay::read(unsigned long offset)
{
  return buffer[posModulo((writeIndex - offset), delayLength)];
}

void SampleDelay::tick()
{
  writeIndex++;
  writeIndex = posModulo(writeIndex, delayLength);
}
