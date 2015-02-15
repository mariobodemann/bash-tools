all:rgb.c
	gcc -g -lm -o rgb rgb.c
	gcc -g -lm -o rgb-bg rgb.c

clean:
	rm rgb rgb-bg
