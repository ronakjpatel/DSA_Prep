


'''
Approach we are following here,

there are 3 possible approaches by which we can solve this problem
1. running two loops: n^2 complexity not good 
2. sorting the array and then two pointers O(n log n) better that prev 
3. using hashmap linear time n but we compromise on space complexity it is also linear 


here implementing the 3rd stretegy 

we will do it in one pass 

one by one as we encounter next value starting from the beginning we look for its complement value in the hash table

if present we simply return the index of two values that made up to certain sum.
if not present then we store the index element values as key and its index value as a value to that key in hashmap


'''


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    my_map = {}
    
    for i in range(len(nums)):
        curr_looking_for_val = target-nums[i]
        
        if curr_looking_for_val in my_map:
            return [my_map[curr_looking_for_val],i]
            
        my_map[nums[i]]=i
    
    return -1
        
    
    
    
        
        



