#! /bin/bash

echo 'fake it till you make it'

# Try-out for automating the process
# for f in *.cpp; do
#  echo "Found a .cpp file"
# done

# Compile
g++ -c helloWorld.cpp
g++ -c world.cpp

# Link
g++ -o hello.exe helloWorld.o world.o
