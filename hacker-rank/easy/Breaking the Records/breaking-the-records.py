"""
Problem:

Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. 
She tabulates the number of times she breaks her season record for most points and least points in a game. 
Points scored in the first game establish her record for the season, and she begins counting from there.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    minimum, maximum = scores[0], scores[0]
    minCount, maxCount = 0, 0
    for score in scores:
        if score < minimum:
            minimum = score
            minCount += 1
        if score > maximum:
            maximum = score
            maxCount += 1
    return [maxCount, minCount]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
