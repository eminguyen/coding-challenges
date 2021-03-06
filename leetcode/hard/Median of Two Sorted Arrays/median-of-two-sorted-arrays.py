"""
Problem:
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        mergedList = nums1 + nums2
        mergedList = sorted(mergedList)
        if(len(mergedList) % 2 == 0):
            index = len(mergedList) // 2
            return float((mergedList[index - 1] + mergedList[index]) / 2 )
        return float(mergedList[len(mergedList) // 2])
