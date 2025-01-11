import math

find = int(input())
array = [1, 2, 4, 8, 8, 8, 8, 4, 2, 1]

for i in range(len(array)):
    if(array[i] == find):
        if(i == math.ceil(len(array)/2)):
            break
        print(f"Front found {find} at index {i}")
        
    if(array[len(array)-1-i] == find):
        if(i == math.floor(len(array)/2)):
            break
        print(f"Rear found {find} at index {len(array)-1-i}")