all:
	g++ -std=c++11 -L/usr/local/lib/ -I/usr/local/include/ -I/usr/local/include/eigen3 -I./ -O3  slicing.cpp -o slicing -lboost_thread-mt -lboost_system -lCGAL -lgmp -lmpfr
clean:
	rm slicing
