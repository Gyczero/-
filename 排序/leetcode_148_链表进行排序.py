#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-26 19:22
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_148_链表进行排序.py
# @Software: PyCharm

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        思路：在时间复杂度O(nlogN)的情况下和空间复杂度常数级的情况下做排序
        nlogN => 快排quicksort
        最好情况：每次选的pivot几乎能把数据均分成两半，这样递归树的深度就是logN，NlogN
        最坏情况：每次找的pivot将数组分成两部分，其中有一部分是空，这样递归树就变成了一棵倾斜的树。树的深度为n-1,这样时间复杂度就变成了O(N^2).

        这题用快排需要维护一个O(N)的list，用归并排序呢？

        思路1：用递归

        :param head:
        :return:
        """
        # # 先遍历一遍，找到大于head的value，如果有，记录下来, break
        # head_value = head.val
        # pointer = head
        # pre_pointer = pointer
        #
        # while pointer is not None:
        #     if pointer.val <= head.val





