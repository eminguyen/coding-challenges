"""
Problem:

Dan is playing a video game in which his character competes in a hurdle race. Hurdles are of varying heights, 
and Dan has a maximum height he can jump.There is a magic potion he can take that will increase his maximum 
height by 1 unit for each dose. How many doses of the potion must he take to be able to jump all of the hurdles.

Given an array of hurdle heights height, and an initial maximum height Dan can jump, k, determine the minimum 
number of doses Dan must take to be able to clear all the hurdles in the race.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    diff = max(height) - k
    return diff if diff > 0 else 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
