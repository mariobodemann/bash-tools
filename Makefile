all: color rainbow

updatelib:
	curl https://raw.githubusercontent.com/nothings/stb/master/stb_image.h -o stb_image.h

color: color.c color_math.c
	g++ -g -lm -o color color.c color_math.c

rainbow : rainbow.c color_math.c
	g++ -g -lm -o rainbow rainbow.c color_math.c

clean:
	rm color rainbow
