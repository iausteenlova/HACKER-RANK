""" Link of the problem : https://www.hackerrank.com/challenges/s10-basic-statistics/problem"""

>>> MEAN - MEDIAN - MODE <<<

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input(''))
arr = input('').split()
A = list(map(int,arr))
#mean
def mean(x):
    m=0
    for i in x :
        m +=i
    return m/len(x)
#median
def Median(x):
    x.sort()
    dm = divmod(len(x),2)
    if dm[1] == 0:
        M = (x[dm[0]]+x[dm[0]+1])/2
    elif dm[1]==1:
        M = x[dm[0]]
    return M
#mode
def mode(x):
    xx = x.copy()
    dic ={}
    for i in range(len(x)):
        c = 0
        for j in range(len(xx)):
            if x[i] == xx[j]:
                c+=1
        dic[x[i]] = c
    ma = max(list(dic.values()))
    el = []
    for i in dic.keys():
        if dic[i] == ma :
            el.append(i)
    return min(el)
print(f'{mean(A)}')
print(f'{median(A)}')
print(f'{mode(A)}')
