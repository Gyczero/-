#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/29 10:45 上午
# @Author  : Frankie
# @File    : weekly_test_156.py

from typing import List

# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
#         """
#         思路:
#         1、hash记录出现的次数
#         2、次数作为list
#         3、list(set(alist)) 的长度
#         :param arr:
#         :return:
#         """
#         ahash = []
#         for i in arr:
#             ahash[i] = ahash.get(i, 0) + 1
#         count_list = [val for (key, val) in  ahash.items()]
#         count_len = len(count_list)
#         unique_len = len(set(count_list))
#         if count_len == unique_len:
#             return True
#         else:
#             return False


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """
        思路:
        1、两个字符串单字符相减
        2、转化为：数组 => 在maxCost下求最长子序列长度的问题
        3、DP：maxlen(i) = max( maxlen(i-1) + len(array[i]+..<=Maxcost))

        问题：按照这样搞，时间复杂度为O(n^2), 时间复杂度过高
        解决方法：优化到O(n)的时间复杂度

        > 问题模板: 滑动窗口问题
        > 滑动窗口解决的问题类型:
        1、在字符串/数组内部求最大子序列长度等
        :param s:
        :param t:
        :param maxCost:
        :return:
        """
        # 字符串相减获得数组, !!!!
        # 滑动窗口标准形式
        alist = [abs(ord(i) - ord(j)) for i,j in zip(s, t)]
        # start = 0
        # maxlen = 0
        # tem_cost = 0
        #
        # for i in range(len(alist)):
        #     tem_cost += alist[i]
        #     while tem_cost > maxCost:
        #         tem_cost -= alist[start]
        #         start += 1
        #     maxlen = max(maxlen, i-start+1)
        # return maxlen

        # 更加巧妙的形式，因为是求最大的滑动窗口长度，一旦窗口长度固定，后续不能再缩小
        i = 0
        tem_cost = 0
        for j in range(len(alist)):
            tem_cost += alist[j]
            if tem_cost > maxCost:
                tem_cost -= alist[i]
                i += 1
        return len(alist)-i




        # # DP初始化
        # maxlen = []
        # costList = []
        # if alist[0] <= maxCost:
        #     maxlen.append(1)
        #     costList.append(alist[0])
        # else:
        #     maxlen.append(0)
        #     costList.append(0)

        # DP循环，优化
        # for i in range(1, len(alist)):
        #     # 获得以i为序列中元素的子序列在maxCost下的最大长度
        #     temCost = 0
        #     temLen = 0
        #     j = i
        #
        #     # !!! 循环的终止条件一定注意
        #     while j >= 0 and temCost + alist[j] <= maxCost:
        #         temLen += 1
        #         temCost += alist[j]
        #         j -= 1
        #
        #     maxlen.append(max(maxlen[i-1], temLen))

        # return max(maxlen)
