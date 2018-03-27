#include "utilities.h"

long posModulo(long value, long mod)
{
  long r = value % mod;
  return r<0 ? r+mod : r;
}
