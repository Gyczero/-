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

        :param head:
        :param n:
        :return:
        """
