#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-03 11:49
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_5250.py
# @Software: PyCharm

from typing import List

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        # 欧几里德定理求2个数的最大公约数
        # 辗转相除法， 又名欧几里德算法（Euclidean
        # algorithm），是求最大公约数的一种方法。
        # 它的具体做法是：用较小数除较大数，再用出现的余数（第一余数）去除除数，
        # 再用出现的余数（第二余数）去除第一余数，如此反复，直到最后余数是0为止。
        # a1x1+a2x2+...+anxn=k
        # 有解的充要条件是：gcd(a1,a2,a3)==k

        # 求一组数的最大公约数，累计，a+b => 最大公约数，这个数可以继续用吗? => 可以！
        # 一重循环，记录值，重复使用
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)

        d = nums[0]
        for i in nums:
            d = gcd(d, i)
        return d==1




