#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-15 16:26
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_101.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        思路：
        1、镜像对称 => 根节点相同
        2、左子树跟右子树镜像对称
        3、[单独镜像对称] => 递归
        :param root:
        :return:
        """
        if root is None:
            return True

        return self.__is_mirror(root.left, root.right)

    def __is_mirror(self, left: TreeNode, right: TreeNode) -> bool:
        """
        检查两个树是否镜像对象
        :param left:
        :param right:
        :return:
        """
        # 极限条件
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False

        # 递归
        if left.val == right.val and self.__is_mirror(left.left, right.right) and self.__is_mirror(left.right, right.left):
            return True
        else:
            return False

