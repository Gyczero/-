#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 3:36 下午
# @Author  : Frankie
# @File    : leetcode_92_反转链表.py


from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        更改结构代码
        反转从位置 m 到 n 的链表。请使用一趟扫描完成反转
        说明:
        1 ≤ m ≤ n ≤ 链表长度

        示例:
        输入: 1->2->3->4->5->NULL, m = 2, n = 4
        输出: 1->4->3->2->5->NULL

        m_pre, m_pointer, n_pre, n_pointer
        单独实现一个链表的反转

        链表结构的变化
        :param head:
        :param m:
        :param n:
        :return:
        """
        # 极端条件None or m==n ok
        if not head or head.next is None:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        # 双指针
        pre = dummy
        now = head
        iter = 1

        # 跳过部分
        while iter <= m:
            if iter == m:
                reverse_start = pre
                reverse_end = now
            pre = now
            now = now.next
            iter += 1

        # 翻转部分
        while m < iter <= n:
            next_tmp = now.next
            now.next = pre
            pre = now
            now = next_tmp
            iter += 1

        # 最后合并
        reverse_start.next = pre
        reverse_end.next = now
        return dummy.next














