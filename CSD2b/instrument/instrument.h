// Instrument class definition

class Instrument
{
public:
  Instrument(std::string newsound);
  void changeSound(std::string newsound);
  void makeSound();
  void uziSound(int clipsize);
private:
  std::string sound;
};
