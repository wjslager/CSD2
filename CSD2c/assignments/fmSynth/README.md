# CSD2c

- [To-do](to-do)
- [Goals](#goals)
- [Design](#design)

## To-do
- Implementation
- Audio flowchart

## Goals

#### Minimal
- [x] FM synthesizer (1 carrier, 1 modulator)
- [ ] Real-time midi input *(just note-ons)*.
- [x] Envelopes for carrier & modulator *(attack/decay)*
- [x] Commandline control:
  - [x] Random values
  - [ ] Master volume
  - [ ] Carrier/modulator gain
  - [ ] Envelope attack/decay

#### Extra
- [ ] Polyphony *(8 voices?)*
- [x] ADSR envelopes *(note-offs)*
- [ ] More of everything we already have (carriers, modulators, envelopes)
  - [ ] Flexible carrier/modulator routing (using pionters?)
- [ ] External control over parameters:
  - [ ] Midi CC's
  - [ ] Open Sound Control

#### Over-the-top
- [ ] Multitimbrality (multiple synth patches listening to midikeyboard splits)
- [ ] FX (delay, some sort of overdrive)
- [ ] Blockchain!!1

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
  - Process function

- Envelope
  - Line function as seen in Pd/Max
  - Uses the getSample() and tick() functionality in a similar way as the oscillators
- AD / ADSR
  - Process function calls the line() function for each stage of the envelope
