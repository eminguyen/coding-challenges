"""
Problem:

Given a positive integer num, write a function which returns True if num is a perfect square else False.
"""

class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num**0.5 - int(num**0.5) == 0
