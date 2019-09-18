#!/usr/bin/env python
# coding: utf-8

# In[1]:


from textwrap import wrap as wp

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = textwrap(string, max_width)
    print(result)
def textwrap(string,width):
    sl = wp(string,width)
    p  = sl.pop()
    for i in range (len(sl)):
        l =str(sl[i])
        print(l)
    return((p))
        

