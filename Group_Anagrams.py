# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 11:21:20 2020

@author: prani
"""

l1 = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(type(sorted(l1[0])))

def grpAnagram(strs):
    final_set = {}
    for x in strs:
        sorted_word = "".join(sorted(x))
        if sorted_word in final_set:
            final_set[sorted_word].append(x)
        else:
            final_set[sorted_word] = [x]

    return(final_set.values())

print(grpAnagram(l1))