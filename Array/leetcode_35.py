#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-03 22:04
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_35.py
# @Software: PyCharm

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        注意点：【极端条件判断】如果target是最小/最大怎么办 | 如果nums是空怎么办
        :param nums:
        :param target:
        :return:
        """
        if not nums:
            return 0
        for index, value in enumerate(nums):
            if value < target:
                continue
            else:
                return index

        return len(nums)
