"""Link : https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem """
# Breaking Records

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    m = scores[0] ; M = scores[0] ; c = 0 ; C = 0
    for i in scores:
        if i > M :
            M = i
            C+=1
        elif i < m :
            m = i
            c+=1
    return C,c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
