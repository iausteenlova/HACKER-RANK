#!/usr/bin/env python
# coding: utf-8


        

"""You have been asked to help study the population of birds migrating across the continent.
Each type of bird you are interested in will be identified by an integer value.
Each time a particular kind of bird is spotted, its id number will be added to your array of sightings.
You would like to be able to find out which type of bird is most common given a list of sightings.
Your task is to print the type number of that bird and if two or more types of birds are equally common,
choose the type with the smallest ID number."""

# hacker rank site : " https://www.hackerrank.com/challenges/migratory-birds/problem "

# solution :

arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))
Q = []
s = set(arr)
Arr = list(s)
for i in Arr:
    k = arr.count(i)
    Q.append(k)
inQ = Q.index(max(Q))
print( Arr[inQ])
