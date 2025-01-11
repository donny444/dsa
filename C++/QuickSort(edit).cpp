//Quick Sort.cpp
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define MAX 12

void showArray(int arr[], int start, int end)
{
	int i;
	for(i=start;i<=end;i++)
		printf("%d ", arr[i]);
}

void doQuickSort(int arr[], int first, int last)
{
	int pos, temp, left, right;
	bool pivot = false;
	left = first;
	right = last;
	pos = first;	//take first element as pivot
	if(first >= last)
		return;
	
	while(!pivot)
	{
		//Compare from right to left
		while(arr[right] >= arr[pos] && right != pos)
			right--;
		if(pos == right)
			pivot = true;
		if(arr[right] < arr[pos])
		{
			//Swapping
			temp = arr[pos];
			arr[pos] = arr[right];
			arr[right] = temp;
			pos = right;
		}
		//Compare from left to right
		while(arr[left] <= arr[pos] && left != pos)
			left++;
		if(pos == left)
			pivot = true;
		if(arr[left] > arr[pos])
		{
			//Swapping
			temp = arr[pos];
			arr[pos] = arr[left];
			arr[left] = temp;
			pos = left;
		}	
	}
	
	doQuickSort(arr, first, pos-1);
	doQuickSort(arr, pos+1, last);
}

int main()
{
	int arr[MAX] = {84, 92, 8, 95, 27, 88, 24, 56, 59, 91, 28, 86};
	int n, i;
	n = 12;
	i = 0;
	printf("Before sort : ");
	showArray(arr, i, n-1);
	printf("\n");
	
	doQuickSort(arr, 0, n-1);
	printf("After sorted : ");
	showArray(arr, i, n-1);
	printf("\n");
	
	return 0;	
}


