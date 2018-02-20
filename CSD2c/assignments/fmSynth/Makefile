CC = g++
CFLAGS = -I/usr/local/include -Wall -std=c++1z
LDFLAGS= -ljack
PG= example

all: $(PG)

$(PG): jack_module.o main.o synth.o fmsynth.o dsp/oscillator.o dsp/sinewave.o dsp/envelope.o dsp/adsr.o
	$(CC) -o $@ $(CFLAGS) jack_module.o main.o synth.o fmsynth.o oscillator.o sinewave.o envelope.o adsr.o $(LDFLAGS)

.cpp.o:
	$(CC) -c $< $(CFLAGS)

clean:
	rm -f *.o
	rm -f $(PG)
