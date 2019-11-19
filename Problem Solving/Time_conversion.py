""" link : https://www.hackerrank.com/challenges/time-conversion/problem """
#   Time Conversion


import os
import sys

def timeConversion(s):
    #     s = input().strip()
    h, m, S = map(int, s[:-2].split(':'))
    p = S[-2:]
    h = h % 12 + (p.upper() == 'PM') * 12
    return (('%02d:%02d:%02d') % (h, m, s))
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

