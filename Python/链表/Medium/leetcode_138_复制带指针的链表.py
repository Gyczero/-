#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 4:26 下午
# @Author  : Frankie
# @File    : leetcode_138_复制带指针的链表.py

from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        思路:
        1、
        :param head:
        :return:
        """