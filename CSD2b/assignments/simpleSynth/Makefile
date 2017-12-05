# Link
main.exe: main.o oscillator.o sinewave.o squarewave.o simplesynth.o
	g++ -o main.exe main.o oscillator.o sinewave.o squarewave.o

# Compile
main.o: main.cpp
	g++ -c main.cpp

simplesynth.o: simplesynth.cpp simplesynth.h
	g++ -c simplesynth.cpp

oscillator.o: oscillator.cpp oscillator.h
	g++ -c oscillator.cpp

sinewave.o: sinewave.cpp sinewave.h
	g++ -c sinewave.cpp

squarewave.o: squarewave.cpp squarewave.h
	g++ -c squarewave.cpp
