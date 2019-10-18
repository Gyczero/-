#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-10 23:58
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_11.py
# @Software: PyCharm

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        注意点：
        1、容器的容积取决于较短的线
        2、构成容积后再移动长的线没有意义
        3、移动短的线，计算面积最大值

        如果两个线相等??? => 任意一个移动均可
        :param height:
        :return:
        """

        i = 0
        j = len(height) - 1
        max_value = 0
        while( i!=j ):
            now_value = min(height[i], height[j]) * (j - i)
            max_value = max(max_value, now_value)

            if height[i] < height[j]:
                i+=1
            else:
                j-=1

        return max_value



