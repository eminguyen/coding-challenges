"""
Problem:

Given a paragraph and a list of banned words, return the most frequent word that is 
not in the list of banned words. It is guaranteed there is at least one word that 
isn't banned, and that the answer is unique.
"""

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        count, common = 0, ""
        for char in paragraph:
            if char in "!?',;.":
                paragraph = paragraph.replace(char,'')
        words = [x.lower() for x in paragraph.split()]
        for i in range(len(words)):
            if words[i] in banned:
                continue
            if words.count(words[i]) > count:
                count = words.count(words[i])
                common = words[i]
        return common
