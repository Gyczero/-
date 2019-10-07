#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-06 23:56
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_69.py
# @Software: PyCharm

class Solution:
    def mySqrt(self, x: int) -> int:
        """
        思路：减少搜索空间 => O(x//2)
        【精彩思路1】牛顿法：


        【精彩思路2】二分查找法：



        :param x:
        :return:
        """
        if x == 0 :
            return 0
        if x < 4:
            return 1

        limit = x // 2

        for i in range(1, limit+2):
            if i*i < x:
                continue
            elif i*i == x:
                return i
            elif i*i > x:
                return i-1
