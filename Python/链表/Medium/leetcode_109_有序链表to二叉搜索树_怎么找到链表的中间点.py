#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 1:01 下午
# @Author  : Frankie
# @File    : leetcode_109_有序链表to二叉搜索树_怎么找到链表的中间点.py


from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """
        思路
        树 -> 递归 -> 中间点进行划分
        关键点：针对链表，怎么找到他的中间点
        极端情况
        找到中间点 => 中间点为root => 递归两边LinkedList
        ### 快慢指针 ###
        :param head:
        :return:
        """
        if not head:
            return None
        if head.next is None:
            return TreeNode(head.val)

        # fs找中间点
        slow = head
        fast = head
        pre = head

        # 此时fast可能为None，所以要增加对fast的判断
        while fast is not None and fast.next is not None:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        root = TreeNode(slow.val)

        pre.next = None
        right_head = slow.next

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(right_head)
        return root









