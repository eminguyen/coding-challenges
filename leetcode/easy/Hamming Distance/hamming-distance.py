"""
Problem:

The Hamming distance between two integers is the number of positions at 
which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
"""

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        for i in range(32):
            if 1 << i & (x ^ y):
                count += 1
        return count
