"""
Problem:

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
"""

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        string = str(num)
        sum = 0
        for i in string:
            sum += int(i)
        if len(str(sum)) <= 1:
            return sum
        else:
            return self.addDigits(sum)
