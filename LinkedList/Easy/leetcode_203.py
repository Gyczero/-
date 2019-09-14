#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-14 12:47
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_203.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 第一个是给定值
        while head is not None:
            if head.val == val:
                head = head.next
            else:
                break

        start = head
        # 全部删完
        if head is None:
            return None

        while head.next is not None :
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return start
