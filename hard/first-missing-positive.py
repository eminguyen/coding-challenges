"""
Problem:

Given an unsorted integer array, find the smallest missing positive integer.
"""

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while(i in nums):
            i+=1
        return i
