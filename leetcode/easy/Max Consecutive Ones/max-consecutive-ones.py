"""
Problem:

Given a binary array, find the maximum number of consecutive 1s in this array.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, 0
        count = 0
        while(j < len(nums)):
            if nums[j] != 1:
                count = max(count, j - i)
                i = j + 1
            j += 1
        return max(count, j - i)
