#ifndef COLOR_MATH
#define COLOR_MATH
typedef enum {
	FOREGROUND,
	BACKGROUND
} Style;

float fclampf(float x, float minValue, float maxValue);

int stringToFloat(char *string, float *result);

int rgbf(float r, float g, float b, Style style);

int hsvToRgb(float h, float s, float v, float *r, float *g, float *b);

#endif
