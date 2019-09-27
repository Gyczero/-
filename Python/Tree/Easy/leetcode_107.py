#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-15 16:40
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_107.py
# @Software: PyCharm

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
        递归 / 迭代
        迭代法思路:
        1、维护2个队列存放当前层的结点和下一层的结点
        2、遍历当前层结点，记录val => 值数组 和left, right=> 下一层结点
        3、遍历完后将value insert(0, [])插入到数据中
        4、下一层结点队列赋值给当前层结点队列，下一层结点队列清空
        :param root:
        :return:
        """
        if root is None:
            return []

        return self.__gen_node_bottoms([root])

    def __gen_node_bottoms(self, nodelist: List[TreeNode]) -> List[List[int]]:
        """
        生成nodelist的bootm遍历
        :param nodelist:
        :return:
        """
        # 递归
        new_node_list = []
        now_values = []

        for node in nodelist:
            now_values.append(node.val)
            if node.left is not None:
                new_node_list.append(node.left)
            if node.right is not None:
                new_node_list.append(node.right)

        # 极限条件
        if len(new_node_list) == 0:
            return [now_values]

        prev_list = self.__gen_node_bottoms(new_node_list)
        prev_list.append(now_values)
        return prev_list


