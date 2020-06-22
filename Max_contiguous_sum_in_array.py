# -*- coding: utf-8 -*-
"""
Created on Sun May 31 09:51:28 2020

@author: prani
"""


def maxcontsum(nums):
    sum_now = nums[0]
    sum_max = nums[0]
    start = 0
    end = 0
    count = 0
    for i in range(1, len(nums)):
        if sum_now < nums[i]:
            count += 1
            sum_now = max(nums[i], sum_now+nums[i] )
        sum_max = max(sum_now, sum_max)

        if sum_max > sum_now:
            start = count
            end = i

    print(start)
    print(end)
    return sum_max


l1 = [-13, -3, -25, -20, -2, -16, -23, -12, -5, -22, -15, -4, -7]
print(maxcontsum(l1))

