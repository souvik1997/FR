all: main

main: slicing.o main.cpp
	g++ -std=c++11 -L/usr/local/lib/ -I/usr/local/include/ -I/usr/local/include/eigen3 -I./ -lboost_thread-mt -lboost_system -lCGAL -lgmp -lmpfr -O3 slicing.o main.cpp -o main

slicing.o: slicing.cpp
	g++ -std=c++11 -I/usr/local/include/ -I/usr/local/include/eigen3 -I./ -O3 -c slicing.cpp -o slicing.o
clean:
	rm main
	rm slicing.o
