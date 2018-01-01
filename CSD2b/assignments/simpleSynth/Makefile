CC = g++

# ==== ==== Link ==== ==== #
main.exe: main.o synth.o simplesynth.o oscillator.o sinewave.o squarewave.o
	$(CC) -o main.exe main.o synth.o simplesynth.o oscillator.o sinewave.o squarewave.o

# ==== ==== Compile ==== ==== #
main.o: main.cpp
	$(CC) -c main.cpp

synth.o: synth.cpp synth.h
	$(CC) -c synth.cpp

simplesynth.o: simplesynth.cpp simplesynth.h
	$(CC) -c simplesynth.cpp

oscillator.o: oscillator.cpp oscillator.h
	$(CC) -c oscillator.cpp

sinewave.o: sinewave.cpp sinewave.h
	$(CC) -c sinewave.cpp

squarewave.o: squarewave.cpp squarewave.h
	$(CC) -c squarewave.cpp
