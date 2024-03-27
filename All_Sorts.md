# Selection Sort

Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted portion of the array and placing it at the beginning. It has a time complexity of O(n^2), making it inefficient on large lists.

## How it Works

1. **Selection**: The algorithm divides the input array into two parts: sorted and unsorted. Initially, the sorted part is empty, and the unsorted part contains the entire array.
2. **Finding Minimum**: It repeatedly finds the minimum element from the unsorted part and swaps it with the first element of the unsorted part.
3. **Expanding Sorted Partition**: After each iteration, the sorted portion expands by one element, and the unsorted portion shrinks by one element.

## Complexity Analysis

- **Time Complexity**: O(n^2) - Selection sort requires two nested loops, resulting in quadratic time complexity.
- **Space Complexity**: O(1) - Selection sort is an in-place sorting algorithm, meaning it doesn't require additional space other than a few variables for swapping.

## Pseudocode

```
function selectionSort(arr)
    n = length of arr
    for i from 0 to n-2
        minIndex = i
        for j from i+1 to n-1
            if arr[j] < arr[minIndex]
                minIndex = j
        if minIndex != i
            swap arr[i] with arr[minIndex]

```

## Example

Consider an array `[64, 25, 12, 22, 11]`:

1. **Initial Array**: `[64, 25, 12, 22, 11]`
2. **After 1st Pass**: `[11, 25, 12, 22, 64]`
3. **After 2nd Pass**: `[11, 12, 25, 22, 64]`
4. **After 3rd Pass**: `[11, 12, 22, 25, 64]`
5. **After 4th Pass**: `[11, 12, 22, 25, 64]` (No change in the 5th pass)

The array is now sorted.

## Conclusion

Selection sort is straightforward to understand and implement but is inefficient for large datasets due to its quadratic time complexity.
