#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 5:11 下午
# @Author  : Frankie
# @File    : leetcode_94_中序遍历.py


from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        递归 + 迭代
        中序：左中右
        :param root:
        :return:
        """

        # # 递归
        # if not root:
        #     return []
        # left_list = self.inorderTraversal(root.left)
        # left_list.append(root.val)
        # right_list = self.inorderTraversal(root.right)
        # left_list += right_list
        # return left_list

        # 迭代 => 基于栈的遍历
        # 栈存储元素
        stack = []
        # 当前指针，指向root
        cur = root
        # 结果list
        res = []

        # 思想：
        # 中序遍历 左中右
        # 1、所有左加入到栈中
        # 2、最后一个左弹出，记录值
        # 3、左值对应右边子树走循环，cur.right，如果right为None且栈中有值，满足继续弹栈
        while cur is not None or len(stack) != 0:
            # 如果右子树为None且栈中有值，继续弹栈

            while cur is not None:
                # 把所有左值结点加到stack中, 把右值也会加入栈
                stack.append(cur)
                cur = cur.left

            # 弹出，记录左值
            cur = stack.pop(-1)
            res.append(cur.val)

            # 按照相同方法记录右子树值
            cur = cur.right
        return res














