#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 11:04 上午
# @Author  : Frankie
# @File    : leetcode_61_链表每个结点向左向右移动k.py


from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        思路:
        1、移动K次 => 写出移动1次的方法 => 循环k次
        2、优化：k次过大时，优化 k % n, 循环n次
        :param head:
        :param k:
        :return:
        """
        if not head:
            return None
        if head.next is None:
            return head

        list_len = 0
        pointer = head
        while pointer is not None:
            pointer = pointer.next
            list_len += 1
        k = k % list_len

        for i in range(k):
            head = self._rotateRightStep(head)
        return head

    def _rotateRightStep(self, head: ListNode) -> ListNode:
        """
        将链表向右移动一位，返回head
        :param head:
        :return:
        """
        pre = head
        pointer = head
        while pointer.next is not None:
            pre = pointer
            pointer = pointer.next

        pointer.next = head
        pre.next = None
        return pointer

