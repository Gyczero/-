#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 10:09 上午
# @Author  : Frankie
# @File    : leetcode_72_编辑距离.py


from typing import List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        是否可以转化成子问题求解
        重点：解决两个子字符串的动态规划问题，一般都是用两个指针i,j, 分别指向两个字符串的最后，
        然后一步步往前走，缩小问题的规模

        字符串 =>
        1、DP建模 => 【循环, 当前状态可用之前状态】 =>
        是不是可以先把word1的一个子串编辑成word2的一个子串？然后随着子串的长度逐渐变大，是否可以推导出结果？
        => 关键，子串
        => dp[i][j] 单词1的[0,i]子串到单词2的[0,j]子串编辑距离
        2、DP方程 => dp[i][j] =
        if word1[i] == word2[j]: dp[i-1][j-1]
        if word1[i] != word2[j]:
        怎么表示单词i到单词j的增删改？
        dp[i-1][j] + 1      delete i处的字符
        dp[i][j-1] + 1      insert i处的字符
        dp[i-1][j-1] + 1    replace i处的字符

        终止条件 base case
        i和j的边界条件
        如果i为0，dp = j
        如果j为0，dp = i
        :param word1:
        :param word2:
        :return:
        """
        # 特别注意：word1和word2可能为"", 空字符串；所以，针对空串，增加大小
        # 必须增加空串，表示初始化，i为空 / j为空！！！
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        # 终止条件
        for i in range(len(word1)+1):
            dp[i][0] = i

        for j in range(len(word2)+1):
            dp[0][j] = j

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1

        return dp[-1][-1]


