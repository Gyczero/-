#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 4:37 下午
# @Author  : Frankie
# @File    : leetcode_235_二叉搜索树的最近公共祖先.py


from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """

        :param root:
        :param p:
        :param q:
        :return:
        """