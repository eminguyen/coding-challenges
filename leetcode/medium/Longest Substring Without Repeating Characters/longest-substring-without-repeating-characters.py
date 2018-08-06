"""
Problem:

Given a string, find the length of the longest substring without repeating characters
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = []
        length,i,j = 0,0,0
        while j < len(s):
            if s[j] not in chars:
                chars.append(s[j])
                j+=1
                length = max(length, j-i)
            else:
                chars.remove(s[i])
                i+=1
        return length
