CC = g++
CFLAGS = -I/usr/local/include -Wall -std=c++1z
LDFLAGS = -lpthread -ljack
PG = example

JACKMOD = jack_module.o ringbuffer.o

all: $(PG)

$(PG): $(JACKMOD) main.o dsp/sampledelay.o wmath.o
	$(CC) -o $@ $(CFLAGS) $(JACKMOD) main.o sampledelay.o wmath.o $(LDFLAGS)

.cpp.o:
	$(CC) -c $< $(CFLAGS)

clean:
	rm -f *.o
	rm -f $(PG)
