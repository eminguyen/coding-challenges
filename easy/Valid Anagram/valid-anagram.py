"""
Problem:

Given two strings s and t , write a function to determine if t is an anagram of s.
"""

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for c in s:
            if c in t:
                t = t.replace(c,'',1)
                s = s.replace(c,'',1)
        if t == '' and s == '':
            return True
        return False
