CC = g++
CFLAGS = -I/usr/local/include -Wall -std=c++1z
LDFLAGS = -lpthread -ljack
PG = example

JACKMOD = jack_module.o ringbuffer.o

DSPREQ = dsp/sampledelay.o dsp/oscillator.o dsp/sinewave.o
DSP = sampledelay.o oscillator.o sinewave.o

all: $(PG)

$(PG): $(JACKMOD) main.o utilities.o $(DSPREQ)
	$(CC) -o $@ $(CFLAGS) $(JACKMOD) main.o utilities.o $(DSP) $(LDFLAGS)

.cpp.o:
	$(CC) -c $< $(CFLAGS)

clean:
	rm -f *.o
	rm -f $(PG)
