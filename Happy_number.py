# -*- coding: utf-8 -*-
"""
Created on Fri May 29 18:41:57 2020

@author: prani

A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the 
squares of its digits, and repeat the process until the number equals 1 (
where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.
"""
#find the no.of digits in n
#


def sumsquared(n):
    sumsq = 0
    while n!= 0:
        sumsq = sumsq + (n%10)**2
        n = n//10

    return sumsq


def IsHappy(n):
    while sumsquared(n)!=1 and sumsquared(n)!=4:
        n = sumsquared(n)
        sumsquared(n)

    if sumsquared(n) == 1:
        return(True)
    elif sumsquared(n) == 4:
        return (False)

#print(sumsquared(19))
print(IsHappy(75))
