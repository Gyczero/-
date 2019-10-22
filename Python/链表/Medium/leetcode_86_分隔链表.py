#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 2:24 下午
# @Author  : Frankie
# @File    : leetcode_86_分隔链表.py

from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        输入: head = 1->4->3->2->5->2, x = 3
        输出: 1->2->2->4->3->5

        两重循环O(n^2)
        for i  1~n
            有比x大
            bigger_pre =pointer
            bpointer
            for  i~n:
                有比x小:
                less_pre = lpointer
                lpointer =

                更改指针：
                lpre.next = bpointer
                bpre.next = lpointer
                tmp = bpointer.next
                bpointer.next = lpointer.next
                lpointer.next = tmp
                continue
                没有比x小：return head

                [1,4,3,2,5,2]
                3
                [1,2,2,4,3,5]

        目的：保留链表原始结构
        更改链表结构时，不进行交换，而进行批量替换
        :param head:
        :param x:
        :return:
        """
        if not head or head.next is None:
            return head
        less_head = ListNode(-1)
        less_pointer = less_head
        big_head = ListNode(-1)
        big_pointer = big_head

        fast = head
        """
        保证原始链表结构的方法：
        快慢慢指针!! 链表：快慢指针~~~ + 递归 + 逻辑方法（繁琐）！！
        """
        while fast is not None:
            if fast.val >= x:
                big_pointer.next = fast
                big_pointer = big_pointer.next
            else:
                less_pointer.next = fast
                less_pointer = less_pointer.next
            fast = fast.next
        big_pointer.next = None
        less_pointer.next = big_head.next
        return less_head.next

        """
        这个方法没办法保证链表的原始结构
        """
        dummy = ListNode(-1000)
        dummy.next = head
        big_pre = dummy
        big_pointer = head
        while big_pointer is not None:
            if big_pointer.val < x:
                big_pre = big_pointer
                big_pointer = big_pointer.next
                continue
            else:
                less_pointer = big_pointer
                less_pre = less_pointer
                # 判断后边有没有比val小的数字
                while less_pointer is not None:
                    if less_pointer.val < x:
                        # 更改链表结构
                        less_pre.next = big_pointer
                        big_pre.next = less_pointer
                        big_pointer.next , less_pointer.next = less_pointer.next, big_pointer.next

                        # big_pointer赋值
                        big_pointer = less_pointer
                        break
                    else:
                        less_pre = less_pointer
                        less_pointer = less_pointer.next
                if less_pointer is None:
                    return dummy.next
        return dummy.next








