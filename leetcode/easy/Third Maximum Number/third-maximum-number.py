"""
Given a non-empty array of integers, return the third maximum number in this array. 

If it does not exist, return the maximum number. The time complexity must be in O(n).
"""

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        order = sorted(list(set(nums)))
        if len(order) >= 3:
            return order[len(order) - 3]
        else:
            return order[len(order) - 1]
