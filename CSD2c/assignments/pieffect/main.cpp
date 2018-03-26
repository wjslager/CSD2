/**********************************************************************
*                     Copyright (c) 2018, Ward Slager
*                        Utrecht, the Netherlands
*                          All rights reserved
***********************************************************************
*  This program is free software: you can redistribute it and/or modify
*  it under the terms of the GNU General Public License as published by
*  the Free Software Foundation, either version 3 of the License, or
*  (at your option) any later version.
*
*  This program is distributed in the hope that it will be useful,
*  but WITHOUT ANY WARRANTY; without even the implied warranty of
*  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*  GNU General Public License for more details.
*
*  You should have received a copy of the GNU General Public License
*  along with this program.
*  If not, see <http://www.gnu.org/licenses/>.
***********************************************************************
*
*  File name     : main.cpp
*  System name   : main
*
*  Description   : Audio effect (delay/reverb)
*
*  Author        : Ward Slager
*  E-mail        : ward.slager@student.hku.nl
*
**********************************************************************/

#include <iostream>
#include <string>
#include <math.h>
#include <thread>
#include "jack_module.h"
#include "dsp/sampledelay.h"
#include "dsp/oscillator.h"
#include "dsp/sinewave.h"
#include "wmath.h"

JackModule jack;
unsigned long samplerate = 48000; // default, overwritten by Jack server
unsigned long buffersize = 128;

// ===== ===== ===== ===== ===== audio thread ===== ===== ===== ===== ===== //

static void audio()
{
  SampleDelay allpass(96000);
  SampleDelay delay1(96000);
  SineWave chorus;
  chorus.setFrequency(0.5, samplerate);
  float *inbuffer = new float[buffersize];
  float *outbuffer = new float[buffersize];

  // The JackModule has created a ringbuffer for both the input and output
  // This will allow us to use our own buffer size instead of the Jack buffer size
  while (true)
  {
    jack.readSamples(inbuffer, buffersize);

    for (unsigned int n = 0; n < buffersize; n++)
    {
      outbuffer[n] = inbuffer[n] + delay1.read(28000 + (200 * chorus.getSample())) + allpass.read(2700);
      allpass.write(outbuffer[n] * 0.1);
      delay1.write(outbuffer[n] * 0.6);

      chorus.tick();
    }

    jack.writeSamples(outbuffer, buffersize);
  }
} // audio()

// ===== ===== ===== ===== ===== main ===== ===== ===== ===== ===== //

int main(int argc, char **argv)
{
  // Start Jack and store the samplerate
  jack.init("pieffect");
  samplerate = jack.getSamplerate();

  std::cerr << "\nSamplerate\t" << samplerate << "\nBuffer size\t" << buffersize << std::endl;

  // Only connect an output
  jack.autoConnect(false, true);

  // Start the DSP thread
  std::thread dspThread(audio);

  // Wait for commandline input
  while(true)
  {
    std::string input;
    std::cin >> input;

    if (input == "q" || input == "e" || input == "quit" || input == "exit") {
      exit(0);
    }
    else {
      std::cerr << "Command not recognized: " << input << std::endl;
    }
  } // while(true)

  dspThread.join();

  // Disconnect Jack and end the program
  jack.end();
  return 0;
} // main()
