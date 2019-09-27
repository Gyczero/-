#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-18 22:12
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_111.py
# @Software: PyCharm


from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
        递归
        注意点: 多种情况下，递归的选择
        二叉树：
        1、空
        2、左子树空
        3、右子树空
        4、左右子树都空
        5、左右子树都有
        :param root:
        :return:
        """
        # 极端条件
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        elif root.left is None:
            return 1+self.minDepth(root.right)
        elif root.right is None:
            return 1+self.minDepth(root.left)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))





