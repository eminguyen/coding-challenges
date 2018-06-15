"""
Problem:

Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
"""

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
