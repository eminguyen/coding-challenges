"""
Problem:

Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.
"""

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums)[-k]
