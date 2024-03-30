
## Top K Element Problem Leetcode: 347

### Problem Statement:
Given a non-empty array of integers, return the k most frequent elements.

### Example:
```plaintext
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```
### My Thoughts:
- HashMap can be utilised here to store the frequency of each element, and then sort the elements based on their frequency. 
- There is linear time solution exist, first store the frequency of each element in a hashmap, then create a list of lists, where each list will contain the elements with the same frequency. **This approach is efficeint and possible because the frequency of elements will be less than or equal to the length of the input array.** we can then iterate from the end of the list of lists and add the elements to the result list until we have k elements in the result list.


