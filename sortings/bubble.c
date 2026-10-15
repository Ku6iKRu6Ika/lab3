#include <stdio.h>
#include <stdlib.h>
#include "saver.h"

int main(int argc, char* argv[])
{
	int wth = atoi(argv[1]);
	int hgt = atoi(argv[2]);

	int** arr = createArr2d(wth, hgt);
	FILE* file = createFile(wth, hgt);
	shuffle2d(arr, wth, hgt, 0);
	writeArray2d(file, arr, wth, hgt);

	int sorted = 0;
	while(!sorted)
	{
		sorted = 1;
		for(int i = 0; i<wth*hgt-1; i++)
		{
			if(arr[i/wth][i%wth]>arr[(i+1)/wth][(i+1)%wth])
			{
				swap(&arr[i/wth][i%wth], &arr[(i+1)/wth][(i+1)%wth]);
				writeSwap(file, i%wth, i/wth, (i+1)%wth, (i+1)/wth);

				sorted = 0;
			}
		}
	}

	
	close(file);

	return 0;
}