#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-14 12:16
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_160.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        思路:
        1、哈希，快速找到headA, 时间:O(n), 空间O(n)
        2、时间: O(n), 空间O(1)的算法：
        => 神奇思路
        => 把两个链表末尾连起来
        => 链表1的长度: x1(到达关键点） + y(后续结点）
        => 链表2的长度: x2(到达关键点) + y(后续结点)
        我们同时遍历链表1和链表2，到达末尾时，再指向另一个链表。
        则当两链表走到相等的位置时：x1+y+x2 = x2+y+x1
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Hash法
        # hash_dict = {}
        # while headA is not None:
        #     hash_dict[headA] = True
        #     headA = headA.next
        #
        # while headB is not None:
        #     if hash_dict.get(headB, False):
        #         return headB
        #     headB = headB.next
        #
        # return None

        # O(n)空间复杂度法
        p = headA
        q = headB
        while p!=q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p

