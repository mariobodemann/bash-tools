all: color rainbow image

updatelib:
	curl https://raw.githubusercontent.com/nothings/stb/master/stb_image.h -o stb_image.h

color: color.cpp color_math.cpp
	g++ -g -lm -o color color.cpp color_math.cpp

rainbow : rainbow.cpp color_math.cpp
	g++ -g -lm -o rainbow rainbow.cpp color_math.cpp

image : image.cpp color_math.cpp
	g++ -g -lm -o image image.cpp color_math.cpp

clean:
	rm color rainbow image
