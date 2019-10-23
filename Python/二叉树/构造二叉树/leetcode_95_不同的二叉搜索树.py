#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 8:06 下午
# @Author  : Frankie
# @File    : leetcode_95_不同的二叉搜索树.py

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        """
        二叉搜索树：
        中节点大于左子树节点，小于右子树节点
        思路：
        1、
        :param n:
        :return:
        """
