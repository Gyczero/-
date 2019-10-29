#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 4:25 下午
# @Author  : Frankie
# @File    : leetcode_215_数组中的第K个最大元素.py

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        思路：
        1、快排：NlogN 时间复杂度随着N过高
        2、尝试优化时间复杂度
        通过堆的方式，优化后的时间复杂度为：O(Nlogk)，空间复杂度O(k)
        维护一个大小为k的小顶堆，堆顶的元素就是第K个元素
        :param nums:
        :param k:
        :return:
        """
        heap = [float("-inf") for i in range(k)]
        for i in nums:
            if i > heap[0]:
                # 弹出堆顶元素
                heapq.heappop(heap)
                # 增加堆中的元素
                heapq.heappush(heap, i)
        return heap[0]


