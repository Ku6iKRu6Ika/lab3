#include <stdio.h>
#include <stdlib.h>
#include "saver.h"

int find(int* src, int el, int N)
{
	if(N == 0)
		return 0;
	int n = N/2;

	if(src[n]>el)
		return find(src, el, n);
	else if(src[n]<el)
		return n+find(src+n, el, N-n);
	else
		return n;

}

void place(int** arr, int wth, int hgt, int* res, int diffX, int diffY, FILE* file)
{
	if(wth == 1 && hgt == 1)
		return;
	int id;
	int i = 0;
	int j = 0;
	int a, b;
	while(i*wth + j < hgt*wth)
	{
		id = find(res, arr[i][j], wth*hgt);

		a = id/wth;
		b = id%wth;

		if(a == i && b == j)
		{
			i += (j+1)/wth;
			j = (j+1)%wth;
			continue;
		}
		
		swap(arr[i]+j, arr[a]+b);
		printf("%d %d %d %d\n", diffX + j, diffY + i, diffX + b, diffY + a);
		writeSwap(file, diffX + j, diffY + i, diffX + b, diffY + a);
	}

	return;
}

int* merge(int** arr1, int wth1, int hgt1, int** arr2, int wth2, int hgt2)
{
	int* res = (int*)malloc(sizeof(int)*(wth1*hgt1 + wth2*hgt2));

	int p1 = 0;
	int p2 = 0;
	int p = 0;
	for(int p = 0; p<wth1*hgt1+wth2*hgt2; p++)
	{
		if(p1 == wth1*hgt1)
		{
			res[p] = arr2[p2/wth2][p2%wth2];
			p2++;
			continue;
		}	
		if(p2 == wth2*hgt2)
		{
			res[p] = arr1[p1/wth1][p1%wth1];
			p1++;
			continue;
		}

		if(arr2[p2/wth2][p2%wth2] > arr1[p1/wth1][p1%wth1])
		{
			res[p] = arr1[p1/wth1][p1%wth1];
			p1++;
			continue;
		}

		else
		{
			res[p] = arr2[p2/wth2][p2%wth2];
			p2++;
			continue;

		}
	}

	return res;
}

int merge2d(int** arr, int wth, int hgt, int diffX, int diffY, FILE* file)
{
	printf("%d %d\n\n", diffX, diffY);
	if(wth == 0)
	{
		wth = 1;
	}
	if(hgt == 0)
	{	
		hgt = 1;
	}

	if(hgt == 1 && wth == 1)
		return 0;

	merge2d(arr, wth/2, hgt/2, diffX, diffY, file);
	merge2d(arr + hgt/2, wth/2, hgt - hgt/2, diffX, diffY+hgt/2, file);

	int** _arr = (int**)malloc(sizeof(int*) * hgt);
	for(int i = 0; i<hgt; i++)
	{
		_arr[i] = arr[i] + wth/2;
	}

	merge2d(_arr, wth - wth/2, hgt/2, diffX+wth/2, diffY, file);
	merge2d(_arr + hgt/2, wth - wth/2, hgt - hgt/2, diffX+wth/2, diffY+hgt/2, file);
	
	int* res;

	res = merge(arr, wth/2, hgt/2, _arr, wth - wth/2, hgt/2);
	place(arr, wth, hgt/2, res, diffX, diffY, file);

	free(res);

	res = merge(arr + hgt/2, wth/2, hgt-hgt/2, _arr + hgt/2, wth-wth/2, hgt-hgt/2);
	place(arr+hgt/2, wth, hgt-hgt/2, res, diffX, diffY, file);
	free(res);

	res = merge(arr, wth, hgt/2, arr+hgt/2, wth, hgt-hgt/2);
	place(arr, wth, hgt, res, diffX, diffY, file);

	free(res);
	
	return 0;
}

int main(int argc, char** argv)
{
	int wth = atoi(argv[1]);
	int hgt = atoi(argv[2]);

	int** arr = createArr2d(wth, hgt);	
	FILE* file = createFile(wth, hgt);
	shuffle2d(arr, wth, hgt, 0);
	writeArray2d(file, arr, wth, hgt);
	print2d(arr, wth, hgt);
	merge2d(arr, wth, hgt, 0, 0, file);

	if(!isSorted(arr, wth, hgt))
		print2d(arr, wth, hgt);

	return 0;
}
