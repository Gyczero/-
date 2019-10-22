#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 10:34 上午
# @Author  : Frankie
# @File    : leetcode_24_两两交换链表中的结点.py

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        给定 1->2->3->4, 你应该返回 2->1->4->3.
        :param head:
        :return:
        """
        # 极端条件处理
        if not head:
            return None
        if head.next is None:
            return head

        i = 1
        pointer = head
        head = head.next

        last_node = None
        while pointer is not None:
            # 链表继续
            if i % 2 != 0:
                pre = pointer
                pointer = pointer.next
                i += 1
            else:
                # 链表翻转，考虑依赖
                if last_node is not None:
                    last_node.next = pointer
                pre.next = pointer.next
                pointer.next = pre
                pointer = pre.next
                last_node = pre
                i += 1
        return head


