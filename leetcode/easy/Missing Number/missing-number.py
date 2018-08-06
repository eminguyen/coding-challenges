"""
Problem:

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
"""

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        i = 0
        while i < len(nums):
            if i != nums[i]:
                break
            i += 1
        return i
