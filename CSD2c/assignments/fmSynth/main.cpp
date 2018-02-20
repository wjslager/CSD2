#include <cmath>
#include <iostream>
#include <thread>
#include "jack_module.h"
#include "synth.h"
#include "fmsynth.h"
// #include "escolors.h"

int main(int argc, char *argv[])
{
  JackModule jack;
  FMSynth synth;

  // Init Jack, exit the program if jack.init returns 1
  if (jack.init("C++ project") == 1) return 1;
  std::cout << "(main) Connected to Jack" << std::endl;

  // Retrieve the samplerate and pass it to all generators
  long unsigned int samplerate = jack.getSamplerate();
  synth.setSamplerate(samplerate);

  // DSP process definition
  jack.onProcess = [&synth](jack_default_audio_sample_t *inBuf, jack_default_audio_sample_t *outBuf, jack_nframes_t nframes, double samplerate)
  {
    synth.process(outBuf, nframes);
    return 0;
  };

  // Ask Jack to connect our audio output to the system output
  jack.autoConnect();
  // All set, let's go!

  // Test stuff
  synth.noteOn(30);
  synth.setGain(0.2);

  // Wait for commanline output while Jack renders our audio
  std::cout << "\nControls:\n'q' to quit\n'n' to randomize note and parameters\n'p' to randomize parameters" << std::endl;

  bool running = true;
  while (running)
  {
    switch (std::cin.get())
    {
      case 'q':
        running = false;
        break;
      case 'n':
        synth.noteOn(30 + (rand() % 36));
        break;
      case 'o':
        synth.noteOff();
        break;
      case 'p':
        synth.fmIndex = rand() % 10000;
        synth.modRatio = rand() % 32;
        synth.carRatio = rand() % 8;
        std::cout << "(main) Randomized note. fmIndex: " << synth.fmIndex << " modulator ratio: " << synth.modRatio << " carrier ratio: " << synth.carRatio << std::endl;
        synth.setFrequency();
        break;
    }
  }

  return 0;
}
