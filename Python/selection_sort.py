number = [1, 9, 3, 7, 8, 6, 2, 4, 5, 0]
def output():
    for i in range(len(number)):
        print(number[i], end=" ")

output()
print("")
for i in range(len(number)-1):
    min = i
    for j in range(i+1, len(number)):
        #count until end, find the minimum number
        if(number[min] > number[j]):
            min = j
    if(min != i):
        #swapping
        temp = number[i]
        number[i] = number[min]
        number[min] = temp
output()