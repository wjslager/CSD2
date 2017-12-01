### Instrument
Pitch in midi notes
- constructor(string "sound")
- setSound(string)
- play(string pitch/articulation)
  - should be called by the subclass
  - pitch/articulation should be optional

### Subclasses

###### Percussion
- constructor()
- note()
  - calls play("normal hit")
- flam(int times)
  - call play("soft hit") multiple times
  - for (int i=0; i<clipsize; i++) play();

###### PitchedInstrument
- constructor(int minPitch, int maxPitch)
- setArticulation(string articulation)
- note(int pitch)
  - calls play("pitch, articulation") if note is in range
- private:
  - articulation
