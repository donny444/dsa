#include<stdio.h>
#include<stdlib.h>

int main()
{
	srand(NULL);
	int number[500];
	int i;
	
	for(i=0;i<500;i++)
		number[i] = rand()%50+1;
	for(i=0;i<500;i++)
		if(number[i]==5)
			printf("Found 5 at %d\n", i);
	
	return 0;
}


