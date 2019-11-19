#!/usr/bin/env python
# coding: utf-8
marksheet=[]
scorelist=[]
if __name__ == '__main__':
        for _ in range(int(input("Enter no. of students"))):
                name = input("name :")
                score = float(input("marks :"))
                marksheet+=[[name,score]]
                scorelist+=[score]
        b=sorted(list(set(scorelist)))[1]
        

        for name,score in sorted(marksheet):
             if score==b:
                    print(f"The second highest scorer is {name}. and the score is {b}.")




