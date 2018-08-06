"""
Problem:

Given an integer, write a function to determine if it is a power of three.
"""

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        while(n > 3):
            n = n / 3
        if n == 3:
            return True
        return False
