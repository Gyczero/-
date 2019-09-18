#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-18 22:41
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_2.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        思路：
        1、遍历 + int + 求和 + 翻转赋值
        :param l1:
        :param l2:
        :return:
        """
        l1_value = ""
        while l1 is not None:
            l1_value = l1_value + str(l1.val)
            l1 = l1.next

        l2_value = ""
        while l2 is not None:
            l2_value = l2_value + str(l2.val)
            l2 = l2.next

        result =  str(int(l1_value[::-1]) + int(l2_value[::-1]))[::-1]
        head = ListNode(0)
        point = head

        # 根据字符串初始化一个链表
        for i in result[:-1]:
            point.val = int(i)
            point.next = ListNode(0)
            point = point.next
        point.val = result[-1]

        return head





