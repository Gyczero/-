#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-13 16:45
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_136.py
# @Software: PyCharm

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        思路1：Hash: 时间复杂度O(n), 维护一个数组元素-出现次数hash, 空间为O(n)
        思路2：异或：时间O(n)，空间为常数
        性质：
        > 交换律：a ^ b ^ c <=> a ^ c ^ b
        > 任何数于0异或为任何数 0 ^ n => n
        > 相同的数异或为0: n ^ n => 0
        :param nums:
        :return:
        """
        ans = 0
        for i in nums:
            ans = ans ^ i
        return ans


if __name__ == '__main__':
    print(Solution().singleNumber([1,2,2,1,3]))
