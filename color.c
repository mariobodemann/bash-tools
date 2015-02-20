#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "color_math.h"

int rgb(char *r, char *g, char *b, Style style);
int hsv(char *h, char *s, char *v, Style style);

void printHelp(const char *program);

int main (int argc, char **argv) {
	if (argc != 5) {
		printHelp(argv[0]);
		return -1;
	} else {
		switch (argv[1][0]) {
		case 'r':
			return rgb( argv[2], argv[3], argv[4], BACKGROUND );
			break;
		case 'R':
			return rgb( argv[2], argv[3], argv[4], FOREGROUND );
			break;
		case 'h':
			return hsv( argv[2], argv[3], argv[4], BACKGROUND );
			break;
		case 'H':
			return hsv( argv[2], argv[3], argv[4], FOREGROUND );
			break;
		default:
			printHelp(argv[0]);
			break;
		}
	}
}

void printHelp(const char *program) {
	printf("Usage: %s [rRhH] [rh] [gs] [bv] \n\n"
		 "\tProduces an escapesequence for a 256 color variant.\n"
		 "\tFirst argument denotes the mode: RGB(rR) or HSV(hH),\n"
		 "\tuse capital letters for foreground, small letters\n"
		 "\tmean background.\n\n"
		 "\tRGB values need to be in the range from 0.0 to 1.0\n"
		 "\tand HSV values in 0.0 to 360.0 for h and 0.0 to 1.0\n"
		 "\tfor s and v.\n", program);
}

int rgb(char *r, char *g, char *b, Style style) {
	float fr, fg, fb;
	if (stringToFloat(r, &fr) &&
		stringToFloat(g, &fg) &&
		stringToFloat(b, &fb) ) {
		return rgbf(fr, fg, fb, style);
	}

	return -1;
}

int hsv(char *h, char *s, char *v, Style style) {
	float fh, fs, fv;

	if (stringToFloat(h, &fh) &&
		stringToFloat(s, &fs) &&
		stringToFloat(v, &fv) ) {

		fh = fclampf(fh, 0, 360);
		fs = fclampf(fs, 0, 1);
		fv = fclampf(fv, 0, 1);

		float r, g, b;
		if (hsvToRgb(fh, fs, fv, &r, &g, &b)) {
			return rgbf(r, g, b, style);
		}
	}
	return -1;
}

