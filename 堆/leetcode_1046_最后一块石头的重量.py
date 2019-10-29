#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 8:28 下午
# @Author  : Frankie
# @File    : leetcode_1046_最后一块石头的重量.py

from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        思路：
        每一回合，从中选出两块最重的石头
        每一回合，从中选出两块最重的石头
        高频 + 选中最大值最小值 => 堆堆堆堆堆堆，高频场景logk, 最大值最小值：大顶堆和小顶堆
        :param stones:
        :return:
        """
        # 初始化一个heap，维护一个堆
        heap = [-i for i in stones]
        """Transform list into a heap, in-place, in O(len(x)) time."""
        heapq.heapify(heap)

        while 1:
            if not heap:
                return 0
            else:
                n1 = heapq.heappop(heap)
                if not heap:
                    return -n1
                n2 = heapq.heappop(heap)
                if n1 != n2:
                    delta = -n1+n2
                    heapq.heappush(heap, -delta)

if __name__ == '__main__':
    print(Solution().lastStoneWeight([2,7,4,1,8,1]))
