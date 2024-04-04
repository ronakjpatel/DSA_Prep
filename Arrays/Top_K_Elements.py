'''
#347 
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
'''

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    
    my_dict = {}
    #iterate through each number
    final_arr=[]
    for num in nums:
        my_dict[num] = my_dict.get(num,0) + 1
    
    aux_array = [[] for x in range(len(nums) + 1 )] #will add one more because we wont use 0 index or 0 freq as a value

    for each_num,freq in my_dict.items():
        aux_array[freq].append(each_num)
        
    for i in range(len(aux_array)-1,0,-1):
        for kk in aux_array[i]:
            final_arr.append(kk)
            if len(final_arr) ==k:
                return final_arr
        
    

    

# num_arr = [1,2]
# k = 2

# print(topKFrequent(num_arr,k))
#efficient solution 




