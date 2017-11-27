// Warnings: programma werkt meestal nog wel
// Errors: compilatie niet voltooid

// argc = Argument count
// argv = Argument vector

// using namespace std;

// includes met <> eromheen skipped zoeken door je eigen files.
// kijkt dus alleen in systeemfiles
#include <iostream>

int main(int argc, char **argv)
{
  std::cout << "Hallo met std endl" << std::endl;
  std::cout << "Hallo met backslash n\n";
  return 0;
}
