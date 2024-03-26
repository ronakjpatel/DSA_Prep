# LeetCode Problem Link: https://leetcode.com/problems/sqrtx/
# Problem Description:
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in C++ or x ** 0.5 in Python.

# My Approach:
# When we know that any number beyond a certain boundary or before a certain boundary is not going to be the solution,
# binary search can be employed.
# Analysis:
# - Binary search allows us to find the square root in logarithmic time complexity O(log n).
# - An alternative linear approach starting from 1 also exists, but its complexity would be O(sqrt(x)),
#   which is slightly higher than O(log n).

class Solution:
    def mySqrt(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid < x:
                # If the square of mid is less than x, move the left pointer to mid + 1
                left = mid + 1
            elif mid * mid > x:
                # If the square of mid is greater than x, move the right pointer to mid - 1
                right = mid - 1
            else:
                # If the square of mid is equal to x, return mid
                return mid
        # If the loop exits, return the value of right (the last valid mid)
        return right
