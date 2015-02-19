all: color rainbow

color: color.c color_math.c
	gcc -O0 -g -lm -o color color.c color_math.c

rainbow : rainbow.c color_math.c
	gcc -g -lm -o rainbow rainbow.c color_math.c

clean:
	rm color rainbow
