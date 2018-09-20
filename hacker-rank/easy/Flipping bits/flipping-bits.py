"""
Problem:

You will be given a list of 32 bit unsigned integers. 
Flip all the bits and and print the result as an unsigned integer.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    return int(bin(n ^ 0xFFFFFFFF), 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
