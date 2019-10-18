#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 10:22 上午
# @Author  : Frankie
# @File    : leetcode_75.py

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        limit = len(nums) - 1
        while i <= limit:
            if nums[i] == 2:
                nums.pop(i)
                nums.append(2)
                limit -= 1
            elif nums[i] == 0:
                nums.pop(i)
                nums.insert(0, 0)
                i += 1
            else:
                i+=1




