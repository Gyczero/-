#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 9:09 下午
# @Author  : Frankie
# @File    : leetcode_105_前序中序.py

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        二叉树前序遍历: 中左右
        二叉树中序遍历: 左中右
        二叉树后序遍历: 左右中
        二叉树 => 通常递归思考
        递归终止条件
        :param preorder:
        :param inorder:
        :return:
        """
        # 终止条件
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        # 根结点 -> 左右子树的前中序遍历
        root_value = preorder[0]
        root_index = inorder.index(root_value)
        left_inorder = inorder[:root_index]
        left_num = root_index
        right_inorder = inorder[root_index+1:]
        left_preorder = preorder[1:1+left_num]
        right_preorder = preorder[1+left_num:]

        root = TreeNode(root_value)
        left = self.buildTree(left_preorder, left_inorder)
        right = self.buildTree(right_preorder, right_inorder)
        root.left = left
        root.right = right
        return root




