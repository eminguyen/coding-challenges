"""
Problem:

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
"""

class Solution:
    def toLowerCase(self, string):
        """
        :type str: str
        :rtype: str
        """
        lowercase = ''
        for c in string:
            if ord(c) >= 65 and ord(c) <= 90 :
                lowercase = lowercase + str(chr(ord(c) + 32))
            else:
                lowercase = lowercase + c
        return lowercase
