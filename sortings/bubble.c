#include <stdio.h>
#include <stdlib.h>
#include "saver.h"

int main(int argc, char** argv)
{
	int wth = (int)*argv[1];
	int hgt = (int)*argv[2];

	int** arr = createArr2d(wth, hgt);
	FILE* file = createFile(wth, hgt);
	shuffle2d(arr, wth, hgt, 0);
	writeArray2d(file, arr, wth, hgt);

	int sorted = 0;
	while(!sorted)
	{
		for(int i = 0; i<wth-1; i++)
		{
			for(int j = 0; j<hgt-1; j++)
			{
				if(arr[j][i] < arr[j+1][i])
				{
					swap(&arr[j][i], &arr[j+1][i]);
					writeSwap(file, i, j, i, j+1);

					sorted = 1;
				}
				else if(arr[j][i] < arr[j][i+1])
				{
					swap(&arr[j][i], &arr[j][i+1]);
					writeSwap(file, i, j, i+1, j);
					if(i<wth-1) i++; 
	
					sorted = 1;
				}
			}
		}
	}

	close(file);

	return 0;
}
