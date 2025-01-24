#include <stdio.h>

main()
{
	char firstArray[] = {"alice", "bob", "trudy", "jack"};
	char secondArray[] = {"janet", "alice", "james", "jack"};
	char result[] = {}
	
	for(i=0;i<firstArray.length;i++)
	{
		for(j=0;j<secondArray.length;j++)
		{
			if(firstArray[i]==secondArray[j])
			{
				result.push(firstArray[i]);
			}
		}
	}
	return result;
}
