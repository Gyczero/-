#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-21 22:09
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_19_删除倒数第N个节点.py
# @Software: PyCharm

from typing import List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：
给定的 n 保证是有效的。

关键：遍历一遍，将链表的node的引用存储到一个数组中
        :param head:
        :param n:
        :return:
        """
        node_list = []
        pointer = head
        while pointer is not None:
            # 这里append是一个引用
            node_list.append(pointer)
            pointer = pointer.next

        # 删除头结点
        if n == len(node_list):
            return head.next
        # 删除尾结点
        elif n == 1:
            node_list[-(n+1)].next = None
        else:
            node_list[-(n+1)].next = node_list[-(n-1)]
        return head


