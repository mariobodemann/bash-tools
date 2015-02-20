#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "color_math.h"

void rainbow( const char *word);

int main (int argc, char **argv) {
	if (argc == 2) {
		rainbow( argv[1] );
	} else {
		rainbow("Please use exactly one text parameter to be rainbowified.");
	}
}

void rainbow (const char *word) {
	float r,g,b,h,s,v;
	size_t len = strlen(word);
	int i = 0;
	for ( i = 0; i < len; ++i) {
		if (hsvToRgb( i * 360.0f / len, 1.0f, 1.0f, &r, &g, &b)) {
			printf("\\[");
			rgbf( r, g, b, FOREGROUND);
			printf("\\]");
			printf("%c", word[i]);
		}
	}
	printf("\e[m");
}
