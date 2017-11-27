# Link
main.exe: cppaint.o figuur.o vierkant.o
	g++ -o cppaint.exe cppaint.o figuur.o vierkant.o

# Compile
paint.o: cppaint.cpp
	g++ -c cppaint.cpp

figuur.o: figuur.cpp figuur.h
	g++ -c figuur.cpp

vierkant.o: vierkant.cpp vierkant.h
	g++ -c vierkant.cpp

clean:
	rm *.o cppaint.exe
