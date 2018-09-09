"""
Problem:

John works at a clothing store. He has a large pile of socks that he must pair by color for sale. 
Given an array of integers representing the color of each sock, determine how many pairs of socks with 
matching colors there are.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sockDict = {}
    number = 0 
    for sock in ar:
        if sock in sockDict:
            if sockDict[sock]:
                sockDict[sock] = False
                number += 1
            else:
                sockDict[sock] = True
        else:
            sockDict[sock]= True
    return number

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
