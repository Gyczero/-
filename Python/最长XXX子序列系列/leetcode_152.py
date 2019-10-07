#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-06 13:47
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_152.py
# @Software: PyCharm

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        思路：
        1、因为是【连续】子序列，后一个状态依赖于前一个数组数据的状态
        2、=> 动态规划
        3、=> 动态转移方程
        维护两个数组
        乘积最大max、负数最小min
        if a[i] > 0 max和min分别赋值
        if a[i] < 0 max和min分别赋值
        if a[i] = 0 返回 0

        整体时间复杂度为O(n)
        :param nums:
        :return:
        """

        # 初始化变量
        max_list = [0 for i in nums]
        min_list = [0 for i in nums]

        # 遍历数组
        for index, value in enumerate(nums):

            # dp初始化
            if index == 0:
                if value > 0:
                    max_list[index] = value
                    min_list[index] = 1
                else:
                    max_list[index] = value
                    min_list[index] = value
                continue

            # 状态转移开始
            if value == 0:
                max_list[index] = 0
                min_list[index] = 0
            elif value > 0:
                max_list[index] = max(max_list[index-1] * value, value)
                min_list[index] = min(min_list[index-1] * value, 1)
            else:
                max_list[index] = max(min_list[index-1] * value, value)
                min_list[index] = min(max_list[index-1] * value, value)

        return max(max_list)





