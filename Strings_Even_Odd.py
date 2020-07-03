# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 23:59:07 2020

@author: prani
"""

t = int(input())
  
for i in range(0,t):
    s = input()
    print(s[::2] + ' '+ s[1::2])

'''    

for i in range(int(input())): s=input()
print(*["".join(s[::2]),"".join(s[1::2])])
'''