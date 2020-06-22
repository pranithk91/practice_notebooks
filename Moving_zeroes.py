# -*- coding: utf-8 -*-
"""
Created on Sat May 30 21:57:58 2020

@author: prani
"""


l1 = [0,1,0,3,12]



nonz = []
z = []

def movezeros(nums):
    

    for x in nums:
        if x == 0:
            z.append(x)

        else:
            nonz.append(x)
    nums.clear()
    nums.extend(nonz+z)


#movezeros(l1)


def move0(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count] = nums[i]
            count = count+1

    while count < len(nums):
        nums[count] = 0
        count = count + 1

move0(l1)
print(l1)
