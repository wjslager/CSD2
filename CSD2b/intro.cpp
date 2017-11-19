// Warnings: programma werkt meestal nog wel
// Errors: dit kan echt niet

// argc = Argument count
// argv = Argument vector

// using namespace std;

// includes met <> eromheen skipped het je eigen files.
// kijkt dus alleen in systeemfiles
#include <iostream>

int main(int argc, char **argv)
{
  std::cout << "Hallo met std endl" << std::endl;
  std::cout << "Hallo met backslash n\n";
  return 0;
}
