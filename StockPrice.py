# -*- coding: utf-8 -*-
"""
Created on Sun May 31 09:42:37 2020

@author: prani
"""

price = [7, 2, 1, 4, 3, 6, 8, 9, 5]

def maxprofit(nums):
    local_max_list = []
    for i, x in enumerate (nums):
        local_max = [(nums[j] - x) for j in range(i+1, len(nums))]
        if local_max != []:
            local_max_list.append(max(local_max))
    maxprofit = max(local_max_list)
    return maxprofit

print(maxprofit(price))

