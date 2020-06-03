#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"

#include "color_math.h"

int image(char *file, int step);

void printHelp(const char *program);

static Style FOREGROUND(false, false);
static Style BACKGROUND(true, false);

int main (int argc, char **argv) {
	if (argc == 2) {
		return image(argv[1], 1);
	} else if (argc == 3) {
		return image(argv[1], atoi(argv[2]));
	} else {
		printHelp(argv[0]);
		return -1;
	}
}

void printHelp(const char *program) {
	printf("Usage: %s IMAGE_PATH [STEP]\n\n"
		 "\tDisplay image in terminal.\n"
		 "\tUse IMAGE_PATH to identify the image.\n"
		 "\tand STEP to the size of the image (Bigger step -> smaller image)\n"
		 , program);
}

int image(char *imageFileName, int step) {
	if (step < 1) {
		fprintf(stderr, "Step of '%d' is to small, please specify a step of at least one\n", step);
		return -2;
	}

	int width, height, components;
	float *data = stbi_loadf(imageFileName, &width, &height, &components, 3);

	if (data == NULL) {
		fprintf(stderr, "Could not load image '%s'\n", imageFileName);
		return -1;
	}

	// cut last line if not displayable
	height = height % 2 == 0 ? height : height - 1;

	for(int y = 0; y < height; y+=2*step) {
		for(int x = 0; x < width; x+=step) {
			float back_r = data[3*x+y*3*width+0];
			float back_g = data[3*x+y*3*width+1];
			float back_b = data[3*x+y*3*width+2];

			float front_r = data[3*width+3*x+y*3*width+0];
			float front_g = data[3*width+3*x+y*3*width+1];
			float front_b = data[3*width+3*x+y*3*width+2];

			printrgbf(back_r, back_g, back_b, BACKGROUND);
			printrgbf(front_r, front_g, front_b, FOREGROUND);
			printf("▄");

		}
		printf("\33[m\n");
	}

	stbi_image_free(data);
	return 1;
}
