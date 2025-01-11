//InsertionSort
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define MAX 10

int main()
{
	int arr[MAX];
	int i, j, k;
	srand(time(NULL));
	for(i=0;i<MAX;i++)
		arr[i] = rand()%30;
	printf("Before sort : ");
	for(i=0;i<MAX;i++)
		printf("%d\t", arr[i]);
	printf("\n");
	
	for(j=1;j<MAX;j++)
	{
		k = arr[j];
		for(i=j-1;i>=0 && k<arr[i];i--)
			arr[i+1] = arr[i];
		arr[i+1] = k;
		printf("take %d to the correct place\n", k);
		for(i=0;i<MAX;i++)
			printf("%d\t", arr[i]);
		printf("\n");
	}
	printf("After sorted : ");
	for(i=0;i<MAX;i++)
		printf("%d\t", arr[i]);
	printf("\n");
	
	return 0;
}


