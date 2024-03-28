# Bubble Sort and Insertion Sort

# ## Bubble Sort: Check -> Swap -> push it to right most
# - Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. It has a time complexity of O(n^2) in the worst case.

# ## Approach:
# - We iterate through the list multiple times, comparing adjacent elements and swapping them if necessary until no more swaps are required, indicating that the list is sorted.

'''
Insertion Sort: Build from left. Check Condition -> Keep Swapping - Done
Insertion Sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It has a time complexity of O(n^2) in the worst case.

Approach:
We divide the input list into two parts: sorted and unsorted. Initially, the sorted part contains only the first element, and the rest of the list is unsorted. We then iterate through the unsorted part, taking one element at a time and inserting 
it into its correct position in the sorted part.'''


'''
Comparison of Selection Sort, Insertion Sort, and Bubble Sort:

Selection Sort:
- How it works: Divides the list into sorted and unsorted regions, selects the minimum element from the unsorted region, and swaps it with the first element of the unsorted region.
- Time Complexity: O(n^2) in all cases.
- Space Complexity: O(1) - In-place sorting algorithm.
- Stability: Not stable.

Insertion Sort:
- How it works: Builds the final sorted array one item at a time by inserting each element into its correct position in the sorted region of the array.
- Time Complexity: 
  - Worst Case: O(n^2).
  - Best Case: O(n).
  - Average Case: O(n^2).
- Space Complexity: O(1) - In-place sorting algorithm.
- Stability: Stable.

Bubble Sort:
- How it works: Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
- Time Complexity: 
  - Worst Case: O(n^2).
  - Best Case: O(n).
  - Average Case: O(n^2).
- Space Complexity: O(1) - In-place sorting algorithm.
- Stability: Stable.

Comparison:
- Efficiency: All have worst-case time complexity of O(n^2), making them inefficient for large datasets. Insertion sort and bubble sort may perform better on partially sorted arrays.
- Stability: Insertion sort and bubble sort are stable, while selection sort is not.
- Space Complexity: O(1) for all.
- Adaptability: Insertion sort and bubble sort can be adaptive, but selection sort is not.
- Implementation Complexity: Insertion sort and bubble sort are generally easier to implement due to simpler logic compared to selection sort.

'''


def bubbleSort(nums):
    """
    Sorts the given list using the Bubble Sort algorithm.

    :param nums: List[int] - The list to be sorted.
    """
    # Iterate over the list in reverse order
    for i in range(len(nums) - 1, -1, -1):
        ptr_left = 0
        ptr_right = 1
        isSwapped = False
            
        # Iterate over the unsorted part of the list
        for j in range(0, i):
            if nums[ptr_left] > nums[ptr_right]:
                # Swap if adjacent elements are in the wrong order
                nums[ptr_left], nums[ptr_right] = nums[ptr_right], nums[ptr_left]
                isSwapped = True
            ptr_left += 1
            ptr_right += 1
        
        # If no swaps were made, the list is sorted
        if not isSwapped:
            print("Loop is breaked")
            break
        
        print("runs")

# Example usage
nums = [0, 4, 1, -1, 3] 
bubbleSort(nums)



def insertionSort(nums):
    """
    Sorts the given list using the Insertion Sort algorithm.

    :param nums: List[int] - The list to be sorted.
    """
    # Iterate over the list
    for i in range(0, len(nums)):
        # Iterate backwards through the sorted region to find the correct position for the current element
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                # Swap elements if they are in the wrong order
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            else:
                # Break the inner loop if the current element is in its correct position
                break
    
    print(nums)

# Example usage
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
insertionSort(nums)
