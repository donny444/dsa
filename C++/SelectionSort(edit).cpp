//Selectionsort.cpp

#include<stdio.h>
#include<stdlib.h>
#define MAX 100
int main()
{
	int i;
	int number[MAX];
	for(i=0;i<MAX;i++)
	{
		number[i] = rand()%250+1;
	}
		
	printf("\n\n");
	int count, min,j ,temp;
	for(count=0;count<MAX-1;count++)
	{
		min = count;
		//count until end, find the minimum number
		for(j=count+1;j<MAX;j++)
		{
			if(number[min] > number[j])
				min = j;
		}
		if(min != count)
		{
			//swap position
			temp = number[count];
			number[count] = number[min];
			number[min] = temp;
		}
	}
	for(i=0;i<MAX;i++)
		printf("%d\t", number[i]);

	return 0;
}


