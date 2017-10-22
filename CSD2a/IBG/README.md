# Irregular Beat Generator
Ward Slager

## Assignment

###### Omschrijving
In dit programma kan de gebruiker de keuze maken uit minimaal twee onregelmatige maatsoorten (bijvoorbeeld
5/4 of 7/8). Het programma genereert vervolgens een beat in de geselecteerde maatsoort en vraagt aan de
gebruiker of hij/zij deze beat wil opslaan. Wanneer de gebruiker de beat wil opslaan, wordt deze geëxporteerd
als midifile. Vervolgens wordt er een nieuwe beat gegenereerd en wordt wederom aan de gebruiker gevraagd
of deze opgeslagen moet worden, etc.

###### Randvoorwaarden
- De ‘Irregular beat generator’ is een command line programma. De interactie met de gebruiker verloopt
via de console (a.k.a. terminal).
- De gegenereerde beats bestaan uit drie verschillende geluiden, verdeeld over het spectrum: low, mid,
high.
- Gebruikers-input: sample files, BPM en maatsoort.
- De beat wordt gegenereerd aan de hand van een algoritme dat rekening houdt met de gekozen
maatsoort (logische ritmische onderverdeling v. low, mid, high) en daarnaast een mate van
randomness hanteert, zodat de resulterende beats elke keer anders zijn.

### Todo
- Make the snaredrum pattern more interesting..
- Bonus stuff:
  - Check all files ending with .wav and load them
  - Option to bypass generation and load from file

## Issues
- **Changing time and then restarting playback without regenerating a beat might trigger an index out of bounds error**
  - Seems to be fixed by triggering regeneration if changing timeBeats
- Clicks when samples are retriggered
- Timing in-between triggers is sloppy

## Design

###### Measure divisions
The algorithm randomly chooses one of three ways of filling a measure. The result is then shuffled and distributed over the kick and snare drum sequences.
The hihat sequences are currently based on always playing when there are no kicks or snares, and randomly playing when there are.

| triggers |         |           |         |
|---------:|:-------:|:---------:|:-------:|
| 4        | 2,2     | -         | -       |
| 5        | 3,2     | -         | -       |
| 6        | 3,3     | 2,2,2     | -       |
| 7        | 3,2,2   | 3,3,1     | -       |
| 8        | 3,3,2   | 4,4       | 4,2,2   |
| 9        | 3,3,3   | 3,2,2,2   | 4,3,2   |
| 10       | 3,3,2,2 | 4,4,2     | 4,3,3   |
| 11       | 3,3,3,2 | 3,2,2,2,2 | 4,3,2,2 |
| 12       | 3,3,3,3 | 4,4,4     | 4,3,3,2 |
