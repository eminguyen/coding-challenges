"""
Problem:

Given a non-empty array of integers, every element appears twice except for one. Find that single one.
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers = []
        for i in nums:
            if i in numbers:
                numbers.remove(i)
            else:
                numbers.append(i)
        return numbers[0]
