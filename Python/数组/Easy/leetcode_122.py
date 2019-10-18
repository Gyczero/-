#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-06 21:40
# @Author  : Frenkie
# @Site    :
# @File    : leetcode_122.py
# @Software: PyCharm

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        四种情况：
        1、先上涨再下降:后一天 - 前一天
        2、先下降后上涨:后一天-前一天
        3、连续上涨、下降：后一天-前一天 | 不买

        #######
        【1，2，5，6】这种情况下在2点也可以买入!!!
        # 前i天的最大收益 = max(前i-1天的最大收益, 前i-1天的最大收益+（第i天的价格-前i-1天最后一次卖出的价格),
        # 前i-2天的最大收益+（i天价格-i-1天价格))
        #
        # 如果后面两个大，前i天的最后一次卖出的价格 = 第i天价格，否则保持原值
        #
        # 数据结构存储:
        # 前i天的最大收益 = dp[]
        # 前i-1天最后一次卖出的价格 = var
        :param prices:
        :return:
        """

        # 思考过于复杂
        # dp = [0 for i in range(len(prices))]
        # before_latest_sold = 0
        #
        # # dp初始化
        # init_value = prices[0]
        # for index, price in enumerate(prices[1:]):
        #     if price > init_value:
        #         # 记录初始化的最大收益
        #         dp[index] = price - init_value
        #         break
        #     else:
        #         init_value = price
        #
        # # dp过程
        # for index, price in enumerate(prices):

        max_profit = 0
        for index in range(1, len(prices)):
            max_profit += max(prices[index] - prices[index-1], 0)
        return max_profit





