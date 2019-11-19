#Quartile's

""" Link : https://www.hackerrank.com/challenges/s10-quartiles/problem """

def Median(x):
    x.sort()
    dm = divmod(len(x),2)
    if dm[1] == 0:
        xx = dm[0]-1
        M = (x[dm[0]]+x[xx])/2
    elif dm[1]==1:
        M = x[dm[0]]
    return (M)
N = int(input(''))
arr = input('').split()
A = list(map(int,arr))
Q2 = Median(A)
EO = divmod(len(A),2)
if EO[1] == 0:
    print(int(Median(A[0:EO[0]])))
    print(int(Median(A)))
    print(int(Median(A[EO[0]:])))
elif EO[1] == 1:
    oo = EO[0]+1
    print(int(Median(A[0:EO[0]])))
    print(int(Median(A)))
    print(int(Median(A[oo:])))
