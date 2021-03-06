#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "color_math.h"

Style::Style()
	: background(false),
	  escape(false) {
}

Style::Style(bool background, bool escape)
	: background(background),
	  escape(escape){
}

float fclampf(float x, float minValue, float maxValue) {
	return fminf(maxValue, fmaxf(minValue, x));
}

int stringToFloat(char *string, float *result) {
	char *end;
	float f = strtof(string, &end);
	if (end != string) {
		*result = f;
		return 1;
	} else {
		return 0;
	}
}

int rgb1to6(float x) {
	return fclampf(x * 6.0f, 0.0f, 5.99f);
}

int rgbTo256(float r, float g, float b) {
	return 16 + (int)(r * 36) + (int)(g * 6) + (int)b;
}

int snprintrgbf(char* output, size_t length, float r, float g, float b, Style style) {
	r = fclampf(r, 0, 1);
	g = fclampf(g, 0, 1);
	b = fclampf(b, 0, 1);
	
	char *sequence = (char*)malloc(MAX_CHARS * sizeof(char));
	char layer = style.background ? 48 : 38;
	int colorCode = rgbTo256(rgb1to6(r), rgb1to6(g), rgb1to6(b));
	int charsPrinted;
	if (style.escape) {
		charsPrinted = snprintf(sequence, MAX_CHARS, "\\[\\e[%02d;5;%dm\\]", layer, colorCode);
	} else {
		charsPrinted = snprintf(sequence, MAX_CHARS, "\\e[%02d;5;%dm", layer, colorCode);
	}

	if ( charsPrinted < length && charsPrinted < MAX_CHARS) {
		strncpy(output, sequence, charsPrinted);
	} else {
		charsPrinted = -1;
	}

	free(sequence);
	return charsPrinted;
}

int printrgbf(float r, float g, float b, Style style) {
	r = fclampf(r, 0, 1);
	g = fclampf(g, 0, 1);
	b = fclampf(b, 0, 1);

	char layer = style.background ? 48 : 38;
	int colorCode = rgbTo256(rgb1to6(r), rgb1to6(g), rgb1to6(b));
	printf("\33[%02d;5;%dm", layer, colorCode);

	return 1;
}

void printrgbend(Style style) {
	if (style.escape) {
		printf("\\[\\e[m\\]");
	} else {
		printf("\\e[m");
	}
}

int hsvToRgb(float h, float s, float v, float *r, float *g, float *b) {
	float c = v * s;
	float x = c * (1.0 - fabsf(fmodf( h / 60.0f, 2.0f) - 1.0f));
	float m = v - c;

	if (0 <= h  && h < 60)        { *r=c; *g=x; *b=0; }
	else if (60 <= h && h < 120)  { *r=x; *g=c; *b=0; }
	else if (120 <= h && h < 180) { *r=0; *g=c; *b=x; }
	else if (180 <= h && h < 240) { *r=0; *g=x; *b=c; }
	else if (240 <= h && h < 300) { *r=x; *g=0; *b=c; }
	else if (300 <= h && h < 360) { *r=c; *g=0; *b=x; }

	*r = *r + m;
	*g = *g + m;
	*b = *b + m;

	return 1;
}

