#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-10 11:15
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_5257.py
# @Software: PyCharm

from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """
        思路:
        1、遍历每个岛屿 => DFS
        2、遍历完成的点怎么办 => 遍历完之后全部用1水域替代

        关键:
        1、矩阵图 => 搜索岛屿、染色等 => DFS递归搜索
        2、树 => 开头的每个结点
           图 => 每一个符合条件的结点
           把图当做树，树的left,right = 图的chooses
        3、想清楚dfs的返回结果，是记录path+Res，还是做个简单的判断，判断是否是封闭岛屿 => 可以先写框架主体，再写终止条件

        DFS: DFS的功能是什么
        1、chooses + 递归 + 和原来结合 + 终止条件
        2、题最关键: 染色的话，染色的时候记得相邻的全部染色，设置flag，而不是直接return; 可能没有染色的会被染色的进行干扰
        :param grid:
        :return:
        """
        res = 0
        # 图的传入参数，针对每个结点都走一遍深度搜索
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    if self.dfs([i, j], grid): res+=1
        return res

    def dfs(self, root, grid):
        """
        dfs遍历:
        【实现的功能】: 图中这个点，搜索这个点的所有邻接点，扩展开来是不是封闭岛屿, 返回true/false
        nums, path, choose, 终止target, res结果
        :return:
        """
        # 深搜开始, 根据root查找chooses
        # 遍历每个节点
        x = root[0]
        y = root[1]

        if x == 0 or x == len(grid)-1 or y == 0 or y == len(grid[0])-1:
            return False

        flag = True
        if grid[x-1][y] == 0:
            grid[x-1][y] = 1
            if not self.dfs([x-1, y], grid): flag = False

        if grid[x+1][y] == 0:
            grid[x+1][y] = 1
            if not self.dfs([x+1, y], grid): flag = False

        if grid[x][y-1] == 0:
            grid[x][y-1] = 1
            if not self.dfs([x, y-1], grid): flag = False

        if grid[x][y+1] == 0:
            grid[x][y+1] = 1
            if not self.dfs([x, y+1], grid): flag = False
        return flag

if __name__ == '__main__':
    print(Solution().closedIsland([[0,0,1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,0,1,1,1],[1,0,1,0,1,1,0,0,0,1],[1,1,1,1,1,1,0,0,0,0],[1,1,1,0,0,1,0,1,0,1],[1,1,1,0,1,1,0,1,1,0]]))














