"""
Problem:

Anna and Brian are sharing a meal at a restuarant and they agree to split the bill equally. 
Brian wants to order something that Anna is allergic to though, and they agree that Anna won't pay for that item.
Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    del bill[k]
    if (sum(bill) // 2) - b == 0:
        print('Bon Appetit')
    else:
        print(abs((sum(bill) // 2) - b))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
