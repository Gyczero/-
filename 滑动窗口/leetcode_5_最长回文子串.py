#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 3:09 下午
# @Author  : Frankie
# @File    : leetcode_5_最长回文子串.py


from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        回文：正读反读都一样
        回文 => 两个字符串 => 不是这种情况
        S=“abacdfgdcaba”  S'=“abacdgfdcaba” 这个反过来就不是回文

        第一个思路：动态规划：
        动态规划方程:
        1、如果bab是回文，那么ababa一定是回文，左右首字母相同 => 转化为公式为:
        P(i,j) = P(i+1, j-1) and si==sj
        P(i,j)代表一串字符串是不是回文

        2、这样情况下，动态规划怎么初始化呢？
        P(i,i) = true
        P(i, i+1) = Si == Si+1

        3、首先初始化一字母和二字母的回文，之后找到三字母的回文，依此类推
        dp[i][j]表示从i到j是否是回文串
        第二个思路：把每个字母当成回文串的中心，考虑两种情况：回文串长度为奇数或者偶数
        for .. 每一个字母  while 满足回文串
        :param s:
        :return:
        """
        # 极端条件
        n = len(s)
        if not s:
            return ""

        res = ""
        dp = [[0] * n for _ in range(n)]
        max_len = float("-inf")
        # dp初始化 + dp推导
        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j] and ((i-j) <=2 or dp[j+1][i-1]):
                    dp[j][i] = 1
                if dp[j][i] and max_len < i-j+1:
                    res = s[j:i+1]
                    max_len = i-j+1
        return res


if __name__ == '__main__':
    print(Solution().longestPalindrome("ac"))