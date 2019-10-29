#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 5:05 下午
# @Author  : Frankie
# @File    : leetcode_264_丑数.py

from typing import List

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        只包含质因数2，3，5的正整数, 三指针法
        丑数 = 2,3,5的倍数
        关键：找到下一个丑数
        dp[i] 表示第i个丑数
        dp[i] = min(2 * dp[1_2], 3*dp[1_3], 5*dp[1_5])
        :param n:
        :return:
        """
        dp = [0] * n
        dp[0] = 1

        # 设置三个指针
        l_2 = 0
        l_3 = 0
        l_5 = 0

        # 遍历计算出下一个丑数
        for i in range(1, n):

            # 下一个丑数迭代公式
            dp[i] = min(2 * dp[l_2], 3 * dp[l_3], 5 * dp[l_5])

            if dp[i] == 2 * dp[l_2]:
                l_2 += 1
            if dp[i] == 3 * dp[l_3]:
                l_3 += 1
            if dp[i] == 5 * dp[l_5]:
                l_5 += 1
        return dp[-1]
