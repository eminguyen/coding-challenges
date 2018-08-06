"""
Problem:

Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindrome = ""
        for center in range(0, len(s)):
            paliOdd = self.findPali(s, center, center)
            paliEven = self.findPali(s, center, center+1)
            if len(paliOdd) > len(palindrome):
                palindrome = paliOdd
            if len(paliEven) > len(palindrome):
                palindrome = paliEven
        return palindrome

    def findPali(self, s, index1, index2):
        """
        :type s: str
        :type index1: int
        :type index2: int
        "rtype: str
        """
        palindrome = ""
        while(index1 >= 0 and index2 < len(s) and s[index1] == s[index2]):
            newPali = s[index1:index2+1]
            index1 -= 1
            index2 += 1
            if(len(newPali) > len(palindrome)):
                palindrome = newPali
        return palindrome
