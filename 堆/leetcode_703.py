#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 4:47 下午
# @Author  : Frankie
# @File    : leetcode_703.py


from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        维护一个k大的小顶堆
        :param k:
        :param nums:
        """
        self.k = k
        self.heap = [float("-inf") for i in range(k)]
        for i in nums:
            if i > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, i)

    def add(self, val: int) -> int:
        """
        增加元素，返回第k大的数
        :param val: logk < k
        :return:
        """
        if val <= self.heap[0]:
            return int(self.heap[0])
        else:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
            return self.heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)