"""
Problem:

Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, 
awarding points on a scale from  to  for three categories: problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet a=(a[0],a[1],a[2]), and 
the rating for Bob's challenge to be the triplet b=(b[0],b[1],b[2].

Your task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

If a[i] > b[i], then Alice is awarded 1 point.
If a[i] < b[i], then Bob is awarded 1 point.
If a[i] = b[i], then neither person receives a point.
Comparison points is the total points a person earned.

Given a and b, determine their respective comparison points.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    points = [0, 0]
    for i in range(3):
        if a[i] > b[i]:
            points[0] += 1
        elif a[i] < b[i]:
            points[1] += 1
    return points

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
