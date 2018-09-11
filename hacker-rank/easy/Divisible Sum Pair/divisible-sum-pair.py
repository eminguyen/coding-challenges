"""
Problem:

You are given an array of n integers, ar = [ar[0], ar[1], .. ar[n-1] , and a positive integer, k. 
Find and print the number of (i,j) pairs where i < j and ar[i] + ar[j] is divisible by k.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    divisible = 0
    for i in range(n):
        for j in range(i+1, n):
            if((ar[i] + ar[j]) % k) == 0:
                divisible += 1
    return divisible

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
