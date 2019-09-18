#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-18 22:26
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_112.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        递归
        :param root:
        :param sum:
        :return:
        """
        if root is None:
            return False

        if root.left is None and root.right is None and root.val == sum:
            return True

        if self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val):
            return True
        else:
            return False

