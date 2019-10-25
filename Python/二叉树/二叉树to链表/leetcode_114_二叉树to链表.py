#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 11:42 上午
# @Author  : Frankie
# @File    : leetcode_114_二叉树to链表.py


from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        二叉树 -> 递归 -> 终止，递归，总结
        """
        if not root:
            return None

        l = self.flatten(root.left)
        r = self.flatten(root.right)

        # 把root.left设置为None，一定要记得把二叉树的left设置为None
        root.left = None
        root.right = l

        pointer = root
        while pointer.right:
            pointer = pointer.right
        pointer.right = r
        return root









