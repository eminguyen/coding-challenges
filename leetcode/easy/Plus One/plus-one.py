"""
Problem:

Given a non-empty array of digits representing a non-negative integer, plus one
to the integer.

The digits are stored such that the most significant digit is at the head of the
 list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number
0 itself.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = -1
        while digits[i] == 9:
            if len(digits) <= -i:
                digits.insert(0,0)
            digits[i] = 0
            i -= 1
        digits[i] += 1
        return digits
