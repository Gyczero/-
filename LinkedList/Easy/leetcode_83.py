#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-13 20:56
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_83.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        遍历一个链表O(n)
        检查后边是否有对对象取值的，如果有，判断对象是否可能为None
        :param head:
        :return:
        """
        if head is None:
            return None
        pointer = head
        while(pointer.next is not None):
            if pointer.next.val == pointer.val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next

        return head




