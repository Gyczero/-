#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-14 18:00
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_234.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """

        :param head:
        :return:
        """
        new_list = []
        while head != None:
            new_list.append(head.val)
            head = head.next
        i = 0
        j = len(new_list) - 1
        while i < j:
            if new_list[i] != new_list[j]:
                return False
            i+=1
            j-=1

        return True

        # 空间复杂度O(1) => 翻转后半部分链表
