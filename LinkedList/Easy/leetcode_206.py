#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-14 17:31
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_206.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        迭代/递归
        :param head:
        :return:
        """
        # 迭代 空间O(n)
        # num_list = []
        # return_start = head
        # pointer = head
        #
        # while head is not None:
        #     num_list.append(head.val)
        #     head = head.next
        #
        # for i in range(-1, -len(num_list)-1, -1):
        #     pointer.val = num_list[i]
        #     pointer = pointer.next
        #
        # return  return_start

        # # 迭代2 空间O(1)
        # prev = None
        # curr = head
        #
        # while curr is not None:
        #     # 记录下一个结点
        #     next_node = curr.next
        #     # 翻转
        #     curr.next = prev
        #     # 记录自身，为下一个结点做准备
        #     prev = curr
        #     # 下一个结点进行判断
        #     curr = next_node
        #
        # return prev

        # 递归，时间O(n), 空间O(n)
        if head is None:
            return head
        if head.next is None:
            return head

        started = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return started





