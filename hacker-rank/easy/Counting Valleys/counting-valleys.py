"""
Problem:

Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. 
During his last hike he took exactly n steps. For every step he took, he noted if it was an uphill, U, or a downhill, D step.


Complete the countingValleys function in the editor below. It must return an integer that denotes the number of valleys Gary traversed. 
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level, count, valley = 0, 0, False
    for i in range(n):
        if s[i] == 'D':
            level -= 1
        else:
            level += 1
        if level < 0 and not valley:
            count += 1
            valley = True
        if level >= 0:
            valley = False
    return count
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
