#leetcode link https://leetcode.com/problems/search-in-rotated-sorted-array/description/

#There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
# such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

'''
first approach should be linear O(n) for searching. but it is not applicable to this situation as 
we are required to do this in O(log n) time so here we have to apply binary search algo.
 
Tips: When you see **search** and **sorted** usually its Binary Search

Key obesevation is we can not blindly eliminate any sides left or right because array is rotated 
so after finding mid point we are required to find the half that could be eliminated.

To implement this,
first you have to identify the sorted half in given array 
and then if the target value does not lie on the sorted half then remove that sorted half. I mean shift the pointers.

Elimination is the key in Binary search. Which portion ? you have to judge. 


However, since the array is possibly rotated at some unknown pivot, we cannot directly apply binary search.
We need to modify it slightly to handle the rotation. The key observation is that one 
of the two halves must be sorted, and the other half must contain the pivot. 
For example, if the array is [4,5,6,7,0,1,2], then the left half [4,5,6,7] is sorted and the right half [0,1,2] contains the pivot. If the array is [7,0,1,2,4,5,6], then the right half [2,4,5,6] is sorted and the left half [7,0,1] contains the pivot.

So, in each iteration of binary search, we first check which half is sorted by comparing the left and middle elements. Then we check if the target is in that sorted half by comparing it with the left and middle elements. If it is in that sorted half, we search in that half as usual. If it is not in that sorted half, we search in the other half that contains the pivot.

For example, if the array is [4,5,6,7,0,1,2] and the target is 0:

We start with left = 0 and right = 6. The middle index is 3 and the middle element is 7.
We see that the left half [4,5,6,7] is sorted and the right half [0,1,2] contains the pivot.
We check if the target 0 is in the left half by comparing it with 4 and 7. It is not in that half because 0 < 4 < 7.
So we search in the right half that contains the pivot by setting left = mid + 1 = 4.
We repeat this process until we find the target or exhaust the search space.


'''
def search(nums, target):
    """
    Search for the target in the rotated sorted array using binary search.

    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            # If target found, return its index
            return mid
        
        # Determine which half is sorted
        if nums[left] <= nums[mid]:
            # Left half is sorted
            if nums[left] <= target < nums[mid]:
                # If target lies within the sorted half, adjust right boundary
                right = mid - 1
            else:
                # Otherwise, adjust left boundary
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                # If target lies within the sorted half, adjust left boundary
                left = mid + 1
            else:
                # Otherwise, adjust right boundary
                right = mid - 1
        
    # Target not found, return -1
    return -1


# print(search([3,1],1))
            
# SLight variation of the above problem
# now instead of having all unique elements in the given nums array 
# what if it has duplicate element ? here now we only want does given target exist in the
# list or not. yes or no we do not want the index at where it is present.

# general tip: when attempting this type of question where there exist some duplicacy 
# than simple try to get rid of that somehow and solve the problem.

'''
Approach for this problem 
Above code will work just fine for our duplicate senario as well untill unless we encounter 
nums[left] = num[mid] = num[right]. this is where we can fail. so to deal with this situation
we simply increase the value of the left pointer and descrese the value of right pointer.
and continue; to the next iteration. 

if nums[left] == num[mid] == num[right]:
    left += 1
    right -= 1
    continue
    
write above code after the first if conidtion of checking the nums[mid] == target and 
you have solved the problem. 
    
'''   
    
    
    
    
    