#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-15 16:38
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_104.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        递归
        :param root:
        :return:
        """

        # 极限条件
        if root is None:
            return 0

        # 递归
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1