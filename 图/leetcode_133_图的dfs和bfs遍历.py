#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 5:25 下午
# @Author  : Frankie
# @File    : leetcode_133_图的dfs和bfs遍历.py

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        :param node:
        :return:
        """
        # lookup = {}
        # def dfs(node):
        #     """
        #     dfs 遍历图
        #     终止条件：None+已经访问过的节点
        #     for nums 过程 choose
        #     :return:
        #     """
        #     if not node:
        #         return
        #
        #     # 防止dfs一直循环下去！！
        #     if node in lookup:
        #         return lookup[node]
        #
        #     clone = Node(node.val, [])
        #     lookup[node] = clone
        #
        #     for n in node.neighbors:
        #         clone.neighbors.append(dfs(n))
        #     return clone
        # return dfs(node)

        from collections import deque
        lookup = {}

        # bfs使用队列实现
        def bfs(node):
            if not node:
                return

            clone = Node(node.val, [])
            lookup[node] = clone

            # 新增一个队列
            queue = deque()
            queue.appendleft(node)

            while queue:
                tmp = queue.pop()
                for n in tmp.neighbors:
                    if n not in lookup:
                        # 新拷贝一个node.val，形成一个新的node
                        lookup[n] = Node(n.val, [])
                        queue.appendleft(n)
                    lookup[tmp].neighbors.append(lookup[n])
            return clone
        return bfs(node)



