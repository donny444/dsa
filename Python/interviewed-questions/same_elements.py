firstArray = ["alice", "bob", "trudy", "jack"]
secondArray = ["janet", "alice", "james", "jack"]
result = []

for i in range(len(firstArray)): # Iterate through the first array
    for j in range(len(secondArray)): # Iterate through the second array
        if firstArray[i] == secondArray[j]: # Name comparison between the two arrays
            result.append(firstArray[i])

print(result)