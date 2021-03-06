"""
Problem:

Given two arrays, write a function to compute their intersection.
"""

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set([i for i in nums1 if i in set(nums2)]))
