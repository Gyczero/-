#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-13 20:33
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_21.py
# @Software: PyCharm

from typing import List
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        思路:
        while l1和l2不是空，一直向新链表中增加Node
        Python 引用和深拷贝
        :param l1:
        :param l2:
        :return:
        """

        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1

        # node初始化，对象要取值，所以增加对None的判断
        if l1.val <= l2.val:
            start_node = l1
            l1 = l1.next
        else:
            start_node = l2
            l2 = l2.next

        pointer_node = start_node
        while (l1 is not None) or (l2 is not None):
            # 一个链表遍历完
            if l1 is None:
                pointer_node.next = l2
                l2 = None
            elif l2 is None:
                pointer_node.next = l1
                l1 = None
            else:
                # l1和l2都不是None，比较值的大小
                if l1.val <= l2.val:
                    pointer_node.next = l1
                    l1 = l1.next
                else:
                    pointer_node.next = l2
                    l2 = l2.next
                pointer_node = pointer_node.next

        return start_node


