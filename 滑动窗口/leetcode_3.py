#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-09 21:07
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_3.py
# @Software: PyCharm

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        最长子串 => 滑动窗口求最大
        解题框架：
        维护一个窗口数组
        遍历所有数据
            窗口数据+1，判断窗口数组是否满足条件
            满足 => 保持原状
            不满足 => 去掉开头一个，窗口保持原来大小
        返回窗口大小，即为最大

        :param s:
        :return:
        """
        window = []
        for i in s:
            window.append(i)
            if len(window) == len(set(window)):
                continue
            else:
                window.pop(0)
        return len(window)