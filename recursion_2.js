#!/usr/bin/node

isSorted = (arr) => {
    if (arr.length == 1)
    {
        return true;
    }
    return arr[0] <= arr[1] && isSorted(arr.slice(1, arr.length))
} 

arr = [1, 2, 3, 4, 5, 6, 7, 8]
console.log(isSorted(arr))

// arr = ["Apple", "Banana", "Cherry", "Pear", "Orange"]
// console.log(arr)

// slc = arr.slice(1, arr.length)
// console.log(slc)

// console.log(arr.length)