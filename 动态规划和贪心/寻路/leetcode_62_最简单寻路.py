#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 10:01 下午
# @Author  : Frankie
# @File    : leetcode_62_最简单寻路.py

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        dfs 时间复杂度始终是2!
        动态规划时间复杂度相对小一些m*n
        典型的动态规划问题:
        dp[m][n] = dp[m-1][n] + dp[m][n-1]
        两个变量，两重循环
        :param m:
        :param n:
        :return:
        """
        # # dp初始化
        # dp = [[0 for i in range(n)] for i in range(m)]
        # # 初始第一行，第一列
        # for i in range(m):
        #     dp[i][0] = 1
        # for j in range(n):
        #     dp[0][j] = 1
        #
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        #
        # return dp[m-1][n-1]

        # 优化空间复杂度, 原来空间复杂度为m*n
        # 优化后为 n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = cur[j] + cur[j-1]

        return cur[-1]









