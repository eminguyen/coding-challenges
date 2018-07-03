"""
Problem:

You are given a string representing an attendance record for a student. The record only contains the following three characters:
    1. 'A' : Absent.
    2. 'L' : Late.
    3. 'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.
"""

class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absences = 0
        late = False
        for i in s:
            if i == "A":
                absences += 1
            if i == "L":
                late += 1
                if late > 2:
                    return False
            else:
                late = 0
        if absences > 1:
            return False
        return True
