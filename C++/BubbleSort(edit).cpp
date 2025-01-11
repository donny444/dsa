//BubbleSort
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<conio.h>
#define MAX 7

int main()
{
	int i, j, temp;
	int number[MAX] = {7,6,1,4,12,9,5};
	for(i=0;i<MAX;i++)
	{
		for(j=0;j<MAX-1-i;j++)
		{
			if(number[j] > number[j+1])
			{
				printf("%d <--> %d\n", number[j], number[j+1]);
				temp = number[j];
				number[j] = number[j+1];
				number[j+1] = temp;
			}
		}
	}
	printf("\nThe numbers after sort\n");
	for(i=0;i<MAX;i++)
	{
		printf("%d\t", number[i]);
	}
	
	return 0;
}


