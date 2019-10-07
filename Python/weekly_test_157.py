#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-06 10:57
# @Author  : Frenkie
# @Site    : 
# @File    : weekly_test_157.py
# @Software: PyCharm

from typing import List

class Solution1:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        """
        1、think less 针对每一个位置遍历 O(n^2)
        2、从数据本身角度：O(n)
        统计奇数和偶数的数量，取最小值
        :param chips:
        :return:
        """
        if not chips:
            return 0

        positions = list(set(chips))
        min_cost = 9999999
        for i in positions:

            # 获得每一个位置的cost
            tem_cost = 0
            for j in chips:
                delta = abs(j-i)%2
                if delta == 0:
                    continue
                else:
                    tem_cost += 1
            if tem_cost < min_cost:
                min_cost = tem_cost

        return min_cost


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """
        1、思路:
        关键 => 最长
        1、两重循环，以每个元素为最后一个的最长定差子序列 => 求最大
        2、dp，通过一个hash存储 => hash存储这个value对应前一个的最大长度。查找 => hash O(n) -> O(1)的复杂度

        格式化思考：

        为什么DP：
        因每个数组值为最后一个值序列，计算最大长度时可以用到前一个序列的最大长度

        => 后一个状态计算可以用前一个状态

        => 思考动态规划的格式化模板

        DP：
        > 【动态规划不一定由紧临的前一个得到，是由前边一个状态得到】
        > 【动态规划保存状态值的容器不一定是数组，可以使hash等】

        后一个状态计算可以用前一个状态
        动态规划的公式为：
        > 状态存储容器: Hash，为什么Hash => 因为需要查找前一个值，查找 => hash
        > 当前状态: DP[i]表示以i为序列最后一个值这个【状态】的最大长度，DP为Hash
        > 前一个状态 DP[当前值 - 差值]

        公式为：DP[i]（当前状态） = DP[a[i]-difference, 0]（前边一个状态） + 1

        公式转为code:
        针对数组遍历进行一重循环：
            公式内容
        求最大
        :param arr:
        :param difference:
        :return:
        """

        max_length = 1
        tem_hash = dict()

        for index, value in enumerate(arr):
            tem_length = tem_hash.get(value-difference ,0) + 1
            tem_hash[value] = tem_length
            if tem_length > max_length:
                max_length = tem_length
        return max_length

        # max_length = 1
        # tem_hash = dict()
        #
        # for index, value in enumerate(arr):
        #     tem_length = 1
        #
        #     for j in range(index-1, -1, -1):
        #         if value - arr[j] != difference:
        #             continue
        #         else:
        #             tem_length += tem_hash[j]
        #             break
        #
        #     # 存储这个index的最大长度
        #     tem_hash[index] = tem_length
        #
        #     if tem_length > max_length:
        #         max_length = tem_length
        #
        # return max_length





