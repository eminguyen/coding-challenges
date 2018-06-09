"""
Problem:

A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number, 
including the bounds if possible.
"""

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        selfDividing = []
        for i in range(left, right+1):
            string = str(i)
            for j in range(len(string)):
                if int(string[j]) == 0:
                    break
                if i % int(string[j]) != 0:
                    break
            else:
                selfDividing.append(i)
        return selfDividing
