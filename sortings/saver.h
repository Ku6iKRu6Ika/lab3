#include <stdio.h>
#include <stdlib.h>

void shuffle2d(int** arr, int width, int height, int seed);

void swap(int* a, int* b);

int writeArray2d(FILE* file, int **arr, int width, int height);

FILE* createFile(int width, int height);

int writeSwap(FILE* file, int, int, int, int);

int close(FILE* file);
