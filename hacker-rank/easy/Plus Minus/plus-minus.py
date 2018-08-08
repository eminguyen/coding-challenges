"""
Problem:

Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. 
Print the decimal value of each fraction on a new line.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive, negative, zero = 0, 0, 0
    length = len(arr)
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    print(positive/length)
    print(negative/length)
    print(zero/length)
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
