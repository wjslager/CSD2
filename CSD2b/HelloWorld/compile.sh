#! /bin/bash

# echo "C++ compile script by Ward Slager"

# Try-out for automating the process
# for f in *.cpp; do
#  echo "Found a .cpp file"
# done

g++ -c helloWorld.cpp
g++ -c world.cpp

# Combine
g++ -o hello.exe helloWorld.o world.o
