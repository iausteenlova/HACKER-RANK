""" link : https://www.hackerrank.com/challenges/mini-max-sum/problem """
# min & max of sum of 4 elements in an array

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    sa = sum(arr);F=[]
    for i in range(len(arr)):
        f = sa - arr[i]
        F.append(f)
    print(f'{min(F)} {max(F)}')
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
