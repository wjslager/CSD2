# CSD2c

- [Project goals](#project goals)
- [Design](#design)

## Project Goals

#### Minimal
- FM synthesizer (1 carrier, 1 modulator)
- Real-time midi input *(just note-ons)*.
- Envelopes for carrier & modulator *(attack/decay)*
- Commandline control:
  - Master volume
  - Carrier/modulator gain
  - Envelope attack/decay

#### Extra
- Polyphony *(8 voices?)*
- ADSR envelopes *(note-offs)*
- More of everything we already have (carriers, modulators, envelopes)
- Midi CC input
- OSC input

#### Over-the-top
- Multitimbrality (multiple synth patches listening to midikeyboard splits)
- FX (delay, some sort of overdrive)

![img](http://78.media.tumblr.com/414c4455bd3a091d939d79e48d86224a/tumblr_ov98ug18Yi1tvvm7oo1_1280.jpg)

---

## Design

#### Class overview
| Base | Derived | |
|-|-|-|
| Oscillator | Sine | |
| Synthesizer | FMSynth | |
| Envelope | AD | ADSR |

#### Class functionality
- FMSynth:
  - Has 2 oscillators (carrier, modulator)
  - Has 2 envelopes (ampEnv, fmEnv)
  - Has functions called noteOn and noteOff which calls all corresponding envelope functions
  - Variables:
    - amplitude
    - frequency
  - Process function:
  ```cpp
  outBuf[i] = modulator.getSample();
  // Apply exponential fm
  carrier.setFrequency(mtof(midi + (outBuf[i] * fmIndex * fmEnv.getSample())));
  outBuf[i] = carrier.getSample() * amplitude;
  modulator.tick();
  fmEnv.tick();
  carrier.tick();
  ```
- Envelope
  - Line function as seen in Pd/Max
    ```cpp
    line(float destination, float frames)
    ```
- AD / ADSR
  - Calls the line() function twice, once for the attack stage, once for the release stage
