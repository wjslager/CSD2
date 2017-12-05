#ifndef _SIMPLESYNTH_H_
#define _SIMPLESYNTH_H_

class SimpleSynth
{
public:
  SimpleSynth();
  ~SimpleSynth();
  void process();
  void setWaveform();
private:
  enum waveType{sine, square};
};

#endif
