#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-14 18:19
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_70.py
# @Software: PyCharm

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        clib(n) = clib(n-1) + clib(n-2)
        :param n:
        :return:
        """

        clib_list = [1, 2]
        for i in range(2, n):
            clib_list.append(clib_list[i-1] + clib_list[i-2])
        return clib_list[n-1]

