all: color rainbow

color: color.cpp color_math.cpp
	g++ -g -lm -o color color.cpp color_math.cpp

rainbow : rainbow.cpp color_math.cpp
	g++ -g -lm -o rainbow rainbow.cpp color_math.cpp

clean:
	rm color rainbow
