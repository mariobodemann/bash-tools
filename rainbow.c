#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "color_math.h"

void rainbow( const char *word, Style style);
int progressArgument( char**, int, int, Style*);
void printHelp( char*);

int main (int argc, char **argv) {
	int seekMoreArguments = 1;
	Style style = DEFAULT;
	for(int i = 1; i < argc; ++i) {
		if (seekMoreArguments && argv[i][0] == '-'){
			seekMoreArguments = progressArgument(argv, argc, i, &style);
		} else {
			rainbow(argv[i], style);
		}
	}
	printrgbend(style);

	return 0;
}

int progressArgument(char **argv, int argc, int arg, Style *style) {
	int seekMoreArguments = 1;
	if (argv[arg][0] == '-') {
		if (argv[arg] - strstr(argv[arg], "bg") <= 2) {
			*style = (Style)(*style ^ BACKGROUND);
		} else if (argv[arg] - strstr(argv[arg], "esc") <= 2) {
			*style = (Style)(*style ^ ESCAPE);
		} else if (argv[arg][1] == '-') {
			seekMoreArguments = 0;
		} else if (argv[arg][1] == 'h') {
			printHelp(argv[arg]);
			seekMoreArguments = 0;
		}
	}

	return seekMoreArguments;
}

void printHelp(char *program) {
	printf("Usage %s [-fg] [-esc] [--]\n", program);
	printf("\n");
	printf("\t-bg  use flip usage of foreground/background (foreground is default)\n");
	printf("\t-esc flip escape color codes with [] from now on (usefull for PS1, default is to not escape)\n");
	printf("\t-h   print this help.\n");
}

void rainbow (const char *word, Style style) {
	float r,g,b,h,s,v;
	size_t len = strlen(word);
	int i = 0;
	for ( i = 0; i < len; ++i) {
		if (hsvToRgb( i * 360.0f / len, 1.0f, 1.0f, &r, &g, &b)) {
			char *color = (char*)calloc(64, sizeof(char));
			int chars = snprintrgbf(color, 64, r, g, b, style);
			if ( chars > 0 ) {
				printf( "%s%c", color, word[i]);
			}
			free(color);
		}
	}
}
