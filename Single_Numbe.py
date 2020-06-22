# -*- coding: utf-8 -*-
"""
Created on Fri May 29 18:11:08 2020

@author: prani
"""
# find out the single number in a list consisting of all the numbers twice except one


def singlenumber(nums):
    for x in nums:
        if nums.count(x) == 1:
            return (x)


#2( a + b + c)-(a + a + b + b + c)
def singlenum(nums):
    print( 2*(sum(set(nums))) - sum(nums))


singlenum([2,2,1,1,5])