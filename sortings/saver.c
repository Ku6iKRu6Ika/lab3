#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "saver.h"
/*
int main(int argc, char** argv)
{
	int** arr = createArr2d(10, 10);

	shuffle2d(arr, 10, 10, 0);

	FILE* file = createFile(10, 10);

	writeArray2d(file, arr, 10, 10);

	swap(arr[1] + 1, arr[2] + 2);

	writeSwap(file, 1, 1, 2, 2);

	close(file);

	return 0;
}
*/
int** createArr2d(int width, int height)
{
	int** arr = (int**)malloc(sizeof(int*)*height);
	for(int i = 0; i<height; i++)
	{
		arr[i] = (int*)malloc(sizeof(int)*width);
		for(int j = 0; j<width; j++)
		{
			arr[i][j] = 10*i+j;
		}
	}

	return arr;
}

void shuffle2d(int **arr, int width, int height, int seed)
{
	if(!seed)
		seed = time(NULL);
	srand(seed);
	int row, column, num;
	for(int i = 0; i<height; i++)
	{
		for(int j = 0; j<width; j++)
		{
			num = rand();
			row = (num>>16) % height;
			column = num % width;
			swap(arr[i] + j, arr[row] + column);
		}
	}

	return;
}

void swap(int* a, int* b)
{
	int tmp = *a;
	*a = *b;
	*b = tmp;
	return;
}

int writeArray2d(FILE* file, int **arr, int width, int height)
{
	int written = 0;
	long int prevPos = ftell(file);
	fseek(file, 1 + 2*sizeof(int), SEEK_SET);
	for(int i = 0; i<height; i++)
		written += fwrite(arr[i], sizeof(int), width, file);

	fseek(file, prevPos, SEEK_SET);

	if(written == width*height)
		return 0;
	return 1;
}

FILE* createFile(int width, int height)
{
	FILE* file = fopen("sequence.txt", "wb");
	size_t size = sizeof(int);
	fwrite(&size, 1, 1, file);
	fwrite(&width, sizeof(int), 1, file);
	fwrite(&height, sizeof(int), 1, file);

	return file;
}


int writeSwap(FILE* file, int x1, int y1, int x2, int y2)
{
	long int prevPos = ftell(file);
	fseek(file, 0, SEEK_END);
	int tmp[4];
	tmp[0] = x1;
	tmp[1] = y1;
	tmp[2] = x2;
	tmp[3] = y2;
	int succ = fwrite(tmp, sizeof(int), 4, file);
	fseek(file, prevPos, SEEK_SET);
	return !(succ == 4);
}

int close(FILE* file)
{
	fclose(file);
	return 0;
}