#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 4:51 下午
# @Author  : Frankie
# @File    : leetcode_103_锯齿形层次遍历.py

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        思路:
        关键：
        锯齿形 => 顺序形在i%2!=0 or i%2==0处进行翻转
        整齐 => 每隔1个进行翻转 => 锯齿形
        :param root:
        :return:
        """
        order_list = self.levelOrder(root)
        for i in range(len(order_list)):
            if i % 2 != 0:
                order_list[i] = order_list[i][::-1]
        return order_list

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        思路：二叉树 => 递归
        :param root:
        :return:
        """
        # 递归终止
        if not root:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]

        res = []
        left_tree = self.levelOrder(root.left)
        right_tree = self.levelOrder(root.right)

        res.append([root.val])
        len_left = len(left_tree)
        len_right = len(right_tree)
        if len_left >= len_right:
            for i in range(len_left):
                right_tem = right_tree[i] if i < len_right else []
                tem = left_tree[i] + right_tem
                res.append(tem)
        else:
            for i in range(len_right):
                left_tem = left_tree[i] if i < len_left else []
                tem = left_tem + right_tree[i]
                res.append(tem)
        return res
