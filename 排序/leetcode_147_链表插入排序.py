#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 2:37 下午
# @Author  : Frankie
# @File    : leetcode_147_链表插入排序.py

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        """
        插入排序
        for 1~n同前边进行对比如果大，放置
        时间复杂度
        O(n^2)
        最好情况下，从小到大排序，O(n)
        :param head:
        :return:
        """
        if not head:
            return None
        if head.next is None:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        now = head
        pre_now = dummy
        pointer = head
        pre_pointer = dummy

        while now:
            while pointer != now:
                if now.val <= pointer.val:
                    pre_now.next = now.next
                    pre_pointer.next = now
                    now.next = pointer
                    now =
                    break
                pre_pointer = pointer
                pointer = pointer.next

            pointer = head
            pre_pointer = dummy
            pre_now = now
            now = now.next
        return dummy.next



