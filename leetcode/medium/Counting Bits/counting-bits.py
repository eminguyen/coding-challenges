"""
Problem:

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num 
calculate the number of 1's in their binary representation and return them as an array.
"""

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        list = []
        for i in range(num + 1):
            list.append(bin(i).count("1"))
        return list
