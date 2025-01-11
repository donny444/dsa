const arr = [1, 2, 3, 7, 8, 9];

function binarySearch(target, start, end) {
    if(start > end) {
        return "Not Found";
    }

    const middle = Math.floor((start + end) / 2);

    if(arr[middle] === target) {
        return `Found it at index ${middle}`;
    }

    if(arr[middle] > target) {
        return binarySearch(target, start, middle - 1);
    }

    if(arr[middle] < target) {
        return binarySearch(target, middle + 1, end);
    }
}

console.log(binarySearch(2, 0, 5));
console.log(binarySearch(9, 0, 5));
console.log(binarySearch(6, 0, 5));