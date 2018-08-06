"""
Problem:

Given an arbitrary ransom note string and another string containing letters
from all the magazines, write a function that will return true if the ransom
note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.
"""

class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for a in ransomNote:
            if a not in magazine:
                return False
            index = magazine.find(a)
            magazine = magazine[:index] + magazine[index+1:]
        return True
