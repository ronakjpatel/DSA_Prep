
# Creating sets s1 and s2 from nums1 and nums2, respectively, 
# requires iterating through each list once, resulting in a time complexity 
# of O(n1 + n2), where n1 is the length of nums1 and n2 is the length of nums2.

# Computing the intersection of two sets using the intersection method 
# typically has a time complexity proportional to the size of the smallest set. 
# In the worst case, where the sets have no common elements, the time 
# complexity is O(min(n1, n2)), where n1 and n2 are the sizes of the sets.

# Therefore, the overall time complexity of the intersection function is 
# dominated by the set operations, which is O(n1 + n2) in the worst case, 
# where n1 and n2 are the lengths of nums1 and nums2, respectively.

def intersection(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        s1 =set(nums1)
        s2 = set(nums2)
        
        print(list(s1.intersection(s2)))
        
intersection([1,2,2,2],[2])

#another approach is sort two arrays and then use two pointer technique one point for
# each array this way you can also solve the program. tim complexity is going to be sligtly 
#higher because of the sorting operation but apart from that it is same complexity as our approach. 