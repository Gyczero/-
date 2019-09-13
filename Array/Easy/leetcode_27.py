#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-02 22:21
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_27.py
# @Software: PyCharm

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        :param nums:
        :param val:
        :return:
        """
        if not nums:
            return 0

        next_assign = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[next_assign] = nums[i]
                next_assign += 1

        return next_assign


