nums = [2, 7, 11, 15]
target = 9

def twosum(arr, target):
    arr.sort()

    left, right = 0, len(arr) - 1
    
    while left < right:
        sum = arr[left] + arr[right]

        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -= 1
    
    return []