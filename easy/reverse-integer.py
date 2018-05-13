"""
Problem:

Given a 32-bit signed integer, reverse digits of an integer.
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string = str(x)
        if x < 0 :
            string = string[1:len(string)] + "-"
        reversed = int(string[::-1])
        if(reversed < -2**31 or reversed > 2**31-1):
            return 0
        return reversed
