#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "color_math.h"

void rainbow( const char *word, Style style);
int rainbowFromFile( const char *file, Style style);
int progressArgument( char**, int, int, Style*);
void printHelp( char*);

int main (int argc, char **argv) {
	int seekMoreArguments = 1;
	Style style;
	for(int i = 1; i < argc; ++i) {
		if (seekMoreArguments && argv[i][0] == '-'){
			seekMoreArguments = progressArgument(argv, argc, i, &style);
		} else if (argv[i][0] != '@' || ! rainbowFromFile(&argv[i][1], style)) {
			rainbow(argv[i], style);
		}
	}
	printrgbend(style);

	return 0;
}

int progressArgument(char **argv, int argc, int arg, Style *style) {
	int seekMoreArguments = 1;
	if (argv[arg][0] == '-') {
		if ((int)strstr(argv[arg], "bg") - (int)argv[arg] <= 2) {
			style->background = true;
		} else if ((int)strstr(argv[arg], "esc") - (int)argv[arg] <= 2) {
			style->escape = true;
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
	printf("Usage %s [-fg] [-esc] [--|@FILE]\n", program);
	printf("\n");
	printf("\t-bg   use flip usage of foreground/background (foreground is default)\n");
	printf("\t-esc  flip escape color codes with [] from now on (usefull for PS1, default is to not escape)\n");
	printf("\t@FILE read text from file\n");
	printf("\t-h   print this help.\n");
}

int rainbowFromFile (const char *file, Style style) {
	char *filename;
	if (strcmp(file, "-") == 0) {
		filename = (char*)calloc(MAX_CHARS, sizeof(char));
		strcpy(filename, "/dev/stdin");
	} else {
		filename = (char*)calloc(MAX_CHARS, sizeof(char));
		strcpy(filename, file);
	}

	FILE *f = fopen(filename, "r");
	if (f) {
		char *line = 0;
		size_t length = 0;
		int charsRead = 1;

		char *complete = 0;

		do {
			charsRead = getline(&line, &length, f);
			if (charsRead > 0) {
				if (!complete) {
					complete = strdup(line);
				} else {
					asprintf(&complete, "%s%s", complete, line);
				}
			}
		} while (charsRead > 0);

		rainbow(complete, style);
		fclose(f);
		return 1;
	} else {
		return 0;
	}
}

void rainbow (const char *word, Style style) {
	float r,g,b,h,s,v;
	size_t len = strlen(word);
	int i = 0;
	for ( i = 0; i < len; ++i) {
		if (hsvToRgb( i * 360.0f / len, 1.0f, 1.0f, &r, &g, &b)) {
			char *color = (char*)calloc(MAX_CHARS, sizeof(char));
			int chars = snprintrgbf(color, MAX_CHARS, r, g, b, style);
			if ( chars > 0 ) {
				printf( "%s%c", color, word[i]);
			}
			free(color);
		}
	}
}
