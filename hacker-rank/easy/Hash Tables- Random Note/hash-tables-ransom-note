"""
Problem:

Complete the checkMagazine function in the editor below. It must print 'Yes' if the note can be formed using the magazine,
or 'No'.

checkMagazine has the following parameters:
- magazine: an array of strings, each a word in the magazine
- note: an array of strings, each a word in the ransom note
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magDict = {}
    for magWord in magazine:
        if magWord not in magDict:
            magDict[magWord] = 1
        else:
            magDict[magWord] += 1
    for word in note: 
        if word not in magDict.keys():
            print('No')
            return
        if magDict[word] >= 1:
            magDict[word] -= 1
        else:
            print('No')
            return
    print('Yes')
    return

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
