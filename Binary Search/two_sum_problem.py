#Leetcode link https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

def fun1(numbers,target):
    left=0
    right=len(numbers)-1 #IMP to do -1 to avoid index out of bounds
    final_index = -1
    
    if target < 0:
        temp_target = 0
    else:
        temp_target=target

    while left <=right:
        mid = (left+right)//2
        if(numbers[mid] < temp_target):
            left=mid+1
        elif(numbers[mid]>temp_target):
            right=mid-1
        else:
            final_index=mid
            break

    if final_index == -1:
        final_index=right

    print("Index is ",final_index)
    left=0
    right=final_index
    while left<right:
        sum_num=numbers[left]+numbers[right]
        if sum_num < target:
            left +=1
        elif sum_num > target:
            right -=1
        else:
            return [left,right]
    return [None,None]
    

print(fun1([-20,-13,-4,-2,-1],-15))