"""
Problem:

Given two strings, determine if they share a common substring. 
A substring may be as small as one character.

For example, the words "a", "and", "art" share the common substring . 
The words "be" and "cat" do not share a substring.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    
    charDict ={}
    for i in s1:
        charDict[i] = True
    for j in s2:
        if j in charDict.keys():
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
