#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 4:40 下午
# @Author  : Frankie
# @File    : leetcode_144_二叉树的前序遍历.py


from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        前序: 中左右
        :param root:
        :return:
        """
        # # 递归
        # if not root:
        #     return []
        #
        # res = [root.val]
        # left = self.preorderTraversal(root.left)
        # right = self.preorderTraversal(root.right)
        # res = res + left + right
        # return res
        if not root:
            return []

        # 迭代方法, 通过stack临时存储树节点
        stack = []
        pointer = root.left
        res = []

        # 根结点入栈
        stack.append(root)
        res.append(root.val)

        # 先把所有中-左压栈，两重循环
        while stack or pointer:
            # 把pointer完全放入栈中
            while pointer:
                stack.append(pointer)
                res.append(pointer.val)
                pointer = pointer.left
            # 弹栈取右边的节点，进行增加值
            pointer = stack.pop(-1).right
        return res






