#number = [7, 6, 1, 4, 12, 9, 5]
number = [53, 52, 51, 50, 49, 48, 47, 46, 982]
def output():
    for i in range(len(number)):
        print(number[i], end=" ")

output()
print("")
for i in range(len(number)):
    for j in range(len(number) - 1):
        if(number[j] > number[j+1]):
            #swapping
            temp = number[j]
            number[j] = number[j+1]
            number[j+1] = temp
output()