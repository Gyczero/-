#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-07 15:11
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_N皇后.py
# @Software: PyCharm

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        思路：
        1、DFS，深度优先遍历（枚举)
        N Queens
        规则：同一行，同一列，同一斜线不能放置相同的元素
        存储：
        DFS -> 第一大层的遍历 for columns
        DFS -> 当前状态 issafe矩阵[][]，主要用来判断，可以用存储的方式，也可以用判断函数
        DFS -> 记录填充path, path []
        DFS -> 最终结果res

        框架：
        极端情况：
        res.append：增加此次结果
        遍历第一层
            判断是否可以放置，如果可以 => 更改状态，增加path
            递归dfs，传入res
            回溯状态，回溯path

        dfs:  维护一个安全矩阵
        dfs2: 状态判断通过函数实现，更快！
        :param n:
        :return:
        """
        res = []
        # 初始化issafe
        issafe = self.__generate_safe_matrix([], n)
        self.__dfs2(0, n, issafe, [], res)

        # 根据res生成最终结果
        res2 = []
        for aresult in res:
            res_list = []
            for acolumn in aresult:
                res_str = "." * acolumn + 'Q' + "." * (n-1-acolumn)
                res_list.append(res_str)
            res2.append(res_list)
        return res2

    def __generate_safe_matrix(self, path, n):
        """
        根据path生成安全矩阵
        :param path:
        :return:
        """
        issafe = [[True for i in range(n)] for j in range(n)]

        if not path:
            return issafe

        for arow, acolumn in enumerate(path):
            # 同一列
            for tem_row in range(n):
                issafe[tem_row][acolumn] = False

            # 同一斜线
            tem_row = arow + 1
            tem_i = acolumn + 1
            while tem_row <= n - 1 and tem_i <= n - 1:
                issafe[tem_row][tem_i] = False
                tem_row += 1
                tem_i += 1

            tem_row = arow + 1
            tem_i = acolumn - 1
            while tem_row <= n - 1 and tem_i >= 0:
                issafe[tem_row][tem_i] = False
                tem_row += 1
                tem_i -= 1
        return issafe

    def __issafe(self, path, row, column):
        """
        根据path判断该行该列是否能放置皇后
        :param path:
        :param row:
        :param column:
        :return:
        """
        for arow, acolumn in enumerate(path):
            # 是否在同一列
            if column == acolumn:
                return False
            # 是否在斜线上
            if abs(row - arow) == abs(column - acolumn):
                return False
        return True

    def __dfs(self, row, column, issafe, path, res):
        """
        :param row: 行序号
        :param column: 可以遍历的行数
        :param issafe: 二维数组
        :param path: 一维数组，每一个可解决方案的路径
        :param res: 结果
        :return:
        """
        # 极端情况
        if len(path) == column:
            res.append(path.copy())
            return

        # 遍历第一层
        for i in range(column):
            if issafe[row][i]:
                path.append(i)
                issafe = self.__generate_safe_matrix(path, column)
                self.__dfs(row+1, column, issafe, path, res)
                path.pop()
                # 回溯状态, 根据
                issafe = self.__generate_safe_matrix(path, column)

    def __dfs2(self, row, column, issafe, path, res):
        """
        :param row: 行序号
        :param column: 可以遍历的行数
        :param issafe: 二维数组
        :param path: 一维数组，每一个可解决方案的路径
        :param res: 结果
        :return:
        """
        # 极端情况
        if len(path) == column:
            res.append(path.copy())
            return

        # 遍历第一层
        for i in range(column):
            if self.__issafe(path, row, i):
                path.append(i)
                self.__dfs2(row+1, column, issafe, path, res)
                path.pop()


if __name__ == '__main__':
    print(Solution().solveNQueens(4))