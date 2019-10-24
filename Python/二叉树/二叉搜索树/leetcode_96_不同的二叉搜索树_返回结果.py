#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 2:04 下午
# @Author  : Frankie
# @File    : leetcode_96_不同的二叉搜索树_返回结果.py

from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        """
        思路：
        二叉搜索树 => 递归思想
        1~n取出数字n，作为root，i-1元素左子树，n-i个元素右子树
        得到左右数据集后，对两个列表进行循环，将左子树右子树连接到root上

        Q: 怎么构造n-i个子树的结点
        A: 新建一个函数，构造i,j之间元素的所有可行trees
        :param n:
        :return:
        """
        if not n:
            return []
        return self._generate_trees(1, n)

    def _generate_trees(self, start:int, end:int) -> List[TreeNode]:
        # 终止条件
        if start > end:
            return [None]
        if start == end:
            return [TreeNode(start)]

        res = []
        for i in range(start, end+1):
            left_trees = self._generate_trees(start, i-1)
            right_trees = self._generate_trees(i+1, end)

            for left_tree in left_trees:
                for right_tree in right_trees:
                    # 这里记得新建一个root，不然会对之前的root进行改变
                    root = TreeNode(i)
                    root.left = left_tree
                    root.right = right_tree
                    res.append(root)
        return res






