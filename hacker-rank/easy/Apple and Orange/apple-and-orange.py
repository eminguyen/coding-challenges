"""
Problem:

Sam's house has an apple tree and an orange tree that yield an abundance of fruit. 
In the diagram below, the red region denotes his house, where  is the start point, and  is the endpoint. 
The apple tree is to the left of his house, and the orange tree is to its right. 
You can assume the trees are located on a single point, where the apple tree is at point , 
and the orange tree is at point .
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    countFruit(s, t, a, apples)
    countFruit(s, t, b, oranges)
    
def countFruit(s, t, treePos, fruits):
    fruitOnHouse = 0
    for fruitPos in fruits:
        landPos = fruitPos + treePos
        if landPos >= s and landPos <= t:
            fruitOnHouse += 1
    print(fruitOnHouse)
            

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
