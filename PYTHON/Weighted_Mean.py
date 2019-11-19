""" Link of the problem : hackerrank.com/challenges/s10-weighted-mean/problem?h_r=next-challenge&h_v=zen"""

>>> WEIGHTED_MEAN <<<

# Enter your code here. Read input from STDIN. Print output to STDOUT
def Wmean(x,xx):
    C=[]
    for i in range(len(x)) :
        c=x[i]*xx[i]
        C.append(c)
    return round(sum(C)/sum(xx),1)
N = int(input(''))
arr = input('').split()
arr2 = input('').split()
A = list(map(int,arr))
A2 = list(map(int,arr2))
print(Wmean(A,A2))
