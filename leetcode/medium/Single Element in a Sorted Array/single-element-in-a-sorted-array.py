"""
Problem:

Given a sorted array consisting of only integers where every element appears twice except for one element which appears once.
Find this single element that appears only once.
"""

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if nums.count(i) == 1:
                return i
