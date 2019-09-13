#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 10:43 PM
# @Author  : taicheng.guo
# @Site    : 
# @File    : leetcode_167.py
# @Software: PyCharm


from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        注意点: 排序数组，唯一解 => 数组首尾双指针
        :param numbers:
        :param target:
        :return:
        """

        lower = 0
        higher = len(numbers) - 1

        tem_sum = numbers[lower] + numbers[higher]
        while(tem_sum != target):
            if tem_sum > target:
                higher -=1
            else:
                lower +=1
            tem_sum = numbers[lower] + numbers[higher]

        return [lower+1, higher+1]

