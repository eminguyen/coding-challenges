"""
Problem:

A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, 
he decides to cancel class if fewer than some number of students are present when class starts.

Given the arrival time of each student and a threshhold number of attendees, determine if the class is canceled.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    count = 0
    for time in a:
        if time <= 0:
            count += 1
    if count < k:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
