### https://www.hackerrank.com/challenges/py-set-add/problem

stamps = []
N = int(input())
for I in range(N):
    s = input()
    stamps.append(s)
    st_set = set(stamps)
print(len(st_set))
    

