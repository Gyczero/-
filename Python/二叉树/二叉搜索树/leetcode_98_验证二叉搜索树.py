#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 3:08 下午
# @Author  : Frankie
# @File    : leetcode_98_验证二叉搜索树.py

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        思想：
        递归 = 递归终止条件 + 递归自调用 + 合并
        左边最右值
        右边最左值
        大于中间值 ok
        :param root:
        :return:
        """
        # 空root或者单节点
        if not root or (root.left is None and root.right is None):
            return True

        left = root.left
        right = root.right
        # 递归整体
        if self.isValidBST(left) and self.isValidBST(right):
            # 单独逻辑
            if left:
                left_big = left
                while left_big.right is not None:
                    left_big = left_big.right
                if left_big.val >= root.val:
                    return False
            if right:
                right_less = right
                while right_less.left is not None:
                    right_less = right_less.left
                if right_less.val <= root.val:
                    return False
            return True
        else:
            return False





