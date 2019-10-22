#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 11:28 上午
# @Author  : Frankie
# @File    : leetcode_82_删除排序链表重复元素.py


from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        思路：
        遍历 -> 删除
        输入: 1->2->3->3->4->4->5
        输出: 1->2->5

        思路：
        1、快慢指针
        2、递归
        :param head:
        :return:
        """

        """
        快慢指针 fast-slow pointer
        快指针跳过有重复的数组，慢指针负责拼接
        经验总结：
        1、链表首个node可以用dummy代表空node
        2、快慢指针 => 两个指针，一个指针判断条件跳过；一个指针拼接
        """
        if head == None or head.next == None:
            return head
        dummy = ListNode(-1000)
        dummy.next = head
        slow = dummy
        fast = dummy.next
        while fast:
            if fast.next and fast.next.val == fast.val:
                tmp = fast.val
                while fast and tmp == fast.val:
                    fast = fast.next
            else:
                slow.next = fast
                slow = fast
                fast = fast.next
        slow.next = fast
        return dummy.next

        """
        自己写的方法，需要考虑的情况和bad case较多
        """
        if not head:
            return None
        if head.next is None:
            return head

        lastNode = None
        pre = head
        pointer = head.next

        while pointer is not None:
            if pointer.val == pre.val:
                same_val = pre.val
                while pre.val == same_val and pre.next is not None:
                    pre = pre.next

                pointer = pre.next
                if pre.next is None and pre.val == same_val:
                    pre = None
            else:
                if not lastNode:
                    lastNode = pre
                    head = pre
                    pre = pre.next
                    pointer = pointer.next
                else:
                    lastNode.next = pre
                    lastNode = pre
                    pre = pre.next
                    pointer = pointer.next

        if not lastNode:
            if not pre:
                return None
            else:
                return pre
        lastNode.next = pre
        return head






