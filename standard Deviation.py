""" Link : https://www.hackerrank.com/challenges/s10-standard-deviation/problem """


import math
from statistics import mean
N = int(input(''))
A = list(map(int,input('').split()))
M = mean(A)
s = 0
for i in A:
    s += (i-M)**2
Std = math.sqrt(s/N)
print(round(Std,1))
