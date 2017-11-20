# Irregular Beat Generator
Ward Slager

## Usage
The Irregular Beat Generator, irBG, generates a rhythm with 3 instruments and then allows you to export this as a midifile. The aim of irBG is to allow a composer to quickly generate a rhythm for composition purposes. It is not meant for live use but can generate new beats on the fly while keeping time.

## The algorithm
The algorithm will generate 2 types of drumhits:
- Hits that always play:
  - These hits will be written to the midifile with velocity 127
- Hits that play 50% of the time:
  - These hits will be written to the midifile with velocity 63

#### Finding the 'important beats'
The algorithm randomly chooses one of three ways of filling a measure as described in the table below.

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

Say the algorithm chooses [3,2,2] this will result in an rhythm consisting of the following triggers:

| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| x | - | - | x | - | x | - |

Now if we shuffle the results the following variations can be made:

| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-----:|
| x | - | - | x | - | x | - | 3 2 2 |
| x | - | x | - | - | x | - | 2 3 2 |
| x | - | x | - | x | - | - | 2 2 3 |

#### Assigning the 'important beats'

Now that we've selected the important beats they are distributed over the kick and snare drum sequences using the following chances:

| Chance | Assigned to         |
|:------:|:-------------------:|
| 40%    | Kick                |
| 40%    | Snare               |
| 20%    | Both kick and snare |

#### Fine tuning the results

- Add a kick at the first beat.
- Remove any snares from the first beat.
- Check if there are any snares at all
  - Insert a snare at the last important beat if no snares are found
- Insert a random kick after each kick that was not preceded by another kick.

#### Generate the hihats
The algorithm will now generate the hihats by either:
- randomly adding a hihat or kick after each trigger without kick or snare
- adding a hihat after each trigger with a snare

If none of the above is done it will add a trigger which will not always play.

## *Assignment as given by the HKU University of the Arts Utrecht:*

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
