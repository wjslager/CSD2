#include <cmath>
#include <iostream>
#include <thread>
#include "jack_module.h"
#include "synth.h"
#include "simplesynth.h"
#include "escolors.h"

int main(int argc, char *argv[])
{
  JackModule jack;
  SimpleSynth synth;

  // Init Jack and retrieve the samplerate from the server
  jack.init("C++ project");
  float samplerate = jack.getSamplerate();
  std::cout << etxt::green << etxt::b << "\nConnected to Jack\n" << etxt::reset << std::endl;

  // DSP process definition
  jack.onProcess = [&synth](jack_default_audio_sample_t *inBuf, jack_default_audio_sample_t *outBuf, jack_nframes_t nframes, double samplerate)
  {
    synth.process(outBuf, nframes);
    return 0;
  };

  // Initiaze DSP stuff now that we now the samplerate of Jack
  std::cout << "========" << std::endl;
  synth.setSamplerate(samplerate);
  synth.setFrequency(440);
  synth.setWave(1);
  synth.setGain(0.1);
  std::cout << "========" << std::endl;

  // Ask Jack to connect our audio output to the system output
  jack.autoConnect();

  // Wait for commanline output while Jack renders our audio
  std::cout << "\nPress 'q' when you want to quit the program." << std::endl;

  bool running = true;
  while (running)
  {
    switch (std::cin.get())
    {
      case 'q':
      running = false;
      break;
    }
  }

  return 0;
}
