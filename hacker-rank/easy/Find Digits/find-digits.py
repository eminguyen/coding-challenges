"""
Problem:

An integer d is a divisor of an integer n if the remainder of n / d = 0.

Given an integer, for each digit that makes up the integer determine whether it is a divisor. 
Count the number of divisors occurring within the integer.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    count = 0
    for i in str(n):
        if int(i) == 0:
            continue
        if n % int(i) == 0:
            count += 1
    return count
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
