#inter Quartile range

""" Link : https://www.hackerrank.com/challenges/s10-interquartile-range/problem """

from statistics import median
n = int(input())
data = list(map(int, input().split()))
freq = list(map(int, input().split()))

s = []
for i in range(n):
    s += [data[i]] * freq[i]
N = sum(freq)
s.sort()
for i in range(0,len(s)):
    s[i] = int(s[i])    
# print(s)
if n%2 != 0:
    q1 = median(s[:N//2])
    q3 = median(s[N//2+1:])
else:
    q1 = median(s[:N//2])
    q3 = median(s[N//2:])

ir = round(float(q3-q1), 1)
print(ir)
