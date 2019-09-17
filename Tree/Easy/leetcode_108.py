#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 12:47 PM
# @Author  : taicheng.guo
# @Site    : 
# @File    : leetcode_108.py
# @Software: PyCharm


from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        思路: 递归
        高度平衡 => 中间点，左右数据量相同
        :param nums:
        :return:
        """
        # 极限条件
        if len(nums) == 0:
            return None

        # 递归
        mid_index = len(nums) // 2
        mid_node = TreeNode(nums[mid_index])
        left_tree = self.sortedArrayToBST(nums[:mid_index])
        if mid_index + 1 >= len(nums):
            right_tree = None
        else:
            right_tree = self.sortedArrayToBST(nums[mid_index+1:])

        mid_node.left = left_tree
        mid_node.right = right_tree
        return mid_node



