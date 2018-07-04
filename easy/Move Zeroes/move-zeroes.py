"""
Problem:

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                nums.append(i)
                nums.remove(i)
