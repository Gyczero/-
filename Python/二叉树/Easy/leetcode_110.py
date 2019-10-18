#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 1:10 PM
# @Author  : taicheng.guo
# @Site    : 
# @File    : leetcode_110.py
# @Software: PyCharm

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        思路：递归
        :param root:
        :return:
        """
        if root is None:
            return True

        if self.isBalanced(root.left) and self.isBalanced(root.right):
            left_depth = self._get_depth(root.left)
            right_depth = self._get_depth(root.right)
            if abs(left_depth - right_depth) <= 1:
                return True
        return False

    def _get_depth(self, root: TreeNode) -> int:
        """
        Get tree depth
        :param root:
        :return:
        """
        # 极端
        if root is None:
            return 0

        # 递归
        return 1 + max(self._get_depth(root.left), self._get_depth(root.right))
