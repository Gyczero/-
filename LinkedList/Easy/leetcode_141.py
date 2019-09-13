#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-13 21:02
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_141.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        思路1：列表存储，空间复杂度O(n)
        思路2：快慢指针: 空间复杂度O(1), 如果是循环链表，快的总会有跟慢的重合的时候
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False

        # 列表存储
        # node_list = []
        # while head.next is not None:
        #     if head  in node_list:
        #         return True
        #     else:
        #         node_list.append(head)
        #         head = head.next
        # return False

        # 快慢指针
        slow = head
        fast = head.next

        # 循环快慢指针
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True






