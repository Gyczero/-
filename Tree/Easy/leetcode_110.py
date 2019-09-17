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


    def _get_depth(self, root: TreeNode) -> int:
        """
        Get tree depth
        :param root:
        :return:
        """
        
