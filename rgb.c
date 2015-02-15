#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef enum {
	FOREGROUND,
	BACKGROUND
} Style;

void printHelp();
int rgb(char *r, char *g, char *b, Style style);

int main (int argc, char **argv) {
	if (argc != 4) {
		printHelp(argv[0]);
		return -1;
	} else {
		if (strstr(argv[0], "rgb-bg")) {
			return rgb( argv[1], argv[2], argv[3], BACKGROUND );
		} else if (strstr(argv[0], "rgb")) { 
			return rgb( argv[1], argv[2], argv[3], FOREGROUND );
		}
	}
}

void printHelp(char *program) {
	printf("Usage:\n%s r g b  produces an escapesequence for a 256 color variant\n", program);
}

float fclampf(float x, float minValue, float maxValue) {
	return fminf(maxValue, fmaxf(minValue, x));
}

int rgb1to6(char *x) {
	char *end;
	float f = strtof( x, &end);
	if (end != x) {
		f = fclampf(f  * 6, 0.0f, 6.0f);
		return (int)(f);
	} else {
		return -1;
	}
}

int rgbTo256(int r, int g, int b) {
	return 16 + r * 36 + g * 6 + b;
}

int rgb(char *r, char *g, char *b, Style style) {
	char *sequence = malloc( 64 * sizeof(char));
	char escape = (style == FOREGROUND) ? 38 : 48;
	int colorCode = rgbTo256(rgb1to6(r), rgb1to6(g), rgb1to6(b));
	int charsPrinted = printf( "\\e[%02d;5;%dm", escape, colorCode);
	return charsPrinted > 0;
}

