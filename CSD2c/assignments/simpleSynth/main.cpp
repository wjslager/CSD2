#include <cmath>
#include <iostream>
#include <thread>
#include "jack_module.h"
#include "synth.h"
#include "simplesynth.h"
// #include "dsp/oscillator.h"
// #include "dsp/sinewave.h"
// #include "dsp/squarewave.h"

int main(int argc, char *argv[])
{
  JackModule jack;
  SimpleSynth synth;

  // DSP definition
  jack.onProcess = [&](jack_default_audio_sample_t *inBuf, jack_default_audio_sample_t *outBuf, jack_nframes_t nframes, double samplerate) {
    synth.process(outBuf, nframes);
    return 0;
  };

  // Jack connection
  jack.init("C++ project");
  jack.autoConnect();
  std::cout << "\033[0;32m\nConnected to Jack succesfully\033[0m\n" << std::endl;

  // Commandline input
  std::cout << "Press 'q' when you want to quit the program." << std::endl;
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

/*
SimpleSynth test(48000);
test.setGain(1);
test.setFrequency(2000);
test.process(samples);

// Print the audio
for (int i=0; i<256; i++) {
  std::cout << samples[i] << std::endl;
}

test.setWave(1);
test.setFrequency(24500); // is above the nyquist so it will not change the frequency
test.setFrequency(8000);
test.setGain(0.5);
test.process(samples);

// Print the audio
for (int i=0; i<256; i++) {
  std::cout << samples[i] << std::endl;
}
*/
