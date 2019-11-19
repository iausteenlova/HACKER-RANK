""" link : https://www.hackerrank.com/challenges/birthday-cake-candles/problem"""
#   Birthday cake candles

import math
import os
import random
import re
import sys

def birthdayCakeCandles(ar):
    m = max(ar);c=0
    for i in ar:
        if i == m:
            c+=1
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
