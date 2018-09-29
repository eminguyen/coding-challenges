"""
Problem:

You are given a string containing characters A and B only. 
Your task is to change it into a string such that there are no matching adjacent characters. 
To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    count = 0
    for i in range(len(s) - 1):
        prevChar = s[i]
        nextChar = s[i+1]
        if prevChar == nextChar:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
