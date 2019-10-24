#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 5:46 下午
# @Author  : Frankie
# @File    : leetcode_257_所有路径.py


from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        """
        二叉树 => 递归
        :param root:
        :return:
        """
        if not root:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]

        # 结合
        left_list = self.binaryTreePaths(root.left)
        right_list = self.binaryTreePaths(root.right)
        left_list += right_list
        for i in range(len(left_list)):
            left_list[i] = str(root.val) + "->" + left_list[i]

        return left_list



