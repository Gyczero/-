#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 1:21 下午
# @Author  : Frankie
# @File    : leetcode_583_两个字符串的删除操作.py

from typing import List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        每部可以任意删除一个字符串中的一个字符
        DP:
        1、建模 dp[i][j]表示word1转为word2需要的编辑距离
        2、dp方程 dp[i][j] = min(dp[i-1][j], dp[i][j-1])
        base case基本情况: 0,0的时候
        :param word1:
        :param word2:
        :return:
        """
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1)+1)]

        # base case
        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j

        # 开始dp
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])+1

        return dp[-1][-1]




