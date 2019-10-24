#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 5:38 下午
# @Author  : Frankie
# @File    : leetcode_113_路径总和.py

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        """
        二叉树 => 递归
        终止，递归使用，返回
        :param root:
        :param sum:
        :return:
        """
        # 终止条件
        if not root:
            return []

        if root.left is None and root.right is None:
            if root.val == sum:
                return [[root.val]]
            else:
                return []

        # 获取左右为sum-root.val的集合
        left_list = self.pathSum(root.left, sum-root.val)
        right_list = self.pathSum(root.right, sum-root.val)
        left_list += right_list

        # 增加root_val
        for alist in left_list:
            alist.insert(0, root.val)
        return left_list
