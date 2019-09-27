#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-15 16:20
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_100.py
# @Software: PyCharm


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        思路：递归
        :param p:
        :param q:
        :return:
        """

        # 极限条件
        if p is None and q is None:
            return True
        elif p is None:
            return False
        elif q is None:
            return False

        # 递归
        if p.val == q.val and  self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        else:
            return False
