#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 22:03
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_121.py
# @Software: PyCharm

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        注意点：
        1、动态规划
        2、取决于该问题是否能用动态规划解决的是这些”小问题“会不会被被重复调用
        前i天最大收益 = max(前i-1天最大收益，第i天的价格 -  前i-1天最小价格) => 一个值记录最大收益，一个值记录最小价格
                    = max(第2天价格-前1天最小价格， 第3天价格 - 前2天最小价格 ...)
        max和min的时间复杂度都是O(n)

        => 单独一个数组存储前N天的最小价格
        => 两个数组相减 => 求max
        :param prices:
        :return:
        """
        if not prices:
            return 0

        min_value = prices[0]
        min_values = [prices[0]]
        for i in range(1, len(prices)):
            if prices[i] < min_value:
                min_values.append(prices[i])
                min_value = prices[i]
            else:
                min_values.append(min_value)

        for i in range(1, len(prices)):
            prices[i] = prices[i] - min_values[i-1]
        prices[0] = 0
        return max(prices)

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))


