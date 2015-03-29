#ifndef COLOR_MATH
#define COLOR_MATH
typedef enum {
	DEFAULT = 0,
	BACKGROUND = 1,
	ESCAPE = 2
} Style;

float fclampf(float x, float minValue, float maxValue);

int stringToFloat(char *string, float *result);

int snprintrgbf(char* output, size_t length, float r, float g, float b, Style style);

void printrgbend( Style style );

int hsvToRgb(float h, float s, float v, float *r, float *g, float *b);

#endif
