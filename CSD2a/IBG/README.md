# Irregular Beat Generator

## Assignment
### Omschrijving
In dit programma kan de gebruiker de keuze maken uit minimaal twee onregelmatige maatsoorten (bijvoorbeeld
5/4 of 7/8). Het programma genereert vervolgens een beat in de geselecteerde maatsoort en vraagt aan de
gebruiker of hij/zij deze beat wil opslaan. Wanneer de gebruiker de beat wil opslaan, wordt deze geëxporteerd
als midifile. Vervolgens wordt er een nieuwe beat gegenereerd en wordt wederom aan de gebruiker gevraagd
of deze opgeslagen moet worden, etc.

### Randvoorwaarden
- De ‘Irregular beat generator’ is een command line programma. De interactie met de gebruiker verloopt
via de console (a.k.a. terminal).
- De gegenereerde beats bestaan uit drie verschillende geluiden, verdeeld over het spectrum: low, mid,
high.
- Gebruikers-input: sample files, BPM en maatsoort.
- De beat wordt gegenereerd aan de hand van een algoritme dat rekening houdt met de gekozen
maatsoort (logische ritmische onderverdeling v. low, mid, high) en daarnaast een mate van
randomness hanteert, zodat de resulterende beats elke keer anders zijn.

## Todo
- Add variation over time: list manipulation
- Clean up the code:
 - Move functions to separate .py files
 - Check for duplicate code?

### Extra
- Check all files ending with .wav and load them
- Option to input each list at booting the program (or load from disk)

## Issues
- Clicks when samples are retriggered
- Timing inbetween triggers is sloppy
- Playback thread keeps running when calling sys.exit() (only an issue when executing the program using IDLE)
