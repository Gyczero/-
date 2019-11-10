#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-10 10:33
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_5255.py
# @Software: PyCharm

from typing import List

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        """
        矩阵
        思路:
        1、 n^2 + 内置
        2、for tuple + for0行 + for 1列+1
        3、遍历矩阵 累加
        :param n:
        :param m:
        :param indices:
        :return:
        """
        matrix = [[0 for _ in range(m)] for _ in range(n)]

        for aindex in indices:
            row = aindex[0]
            col = aindex[1]

            for i in range(m):
                matrix[row][i] += 1

            for i in range(n):
                matrix[i][col] += 1

        res = 0
        for i in range(n):
            for j in range(m):
                res += 1 if matrix[i][j] % 2 != 0 else 0

        return res

if __name__ == '__main__':
    s = Solution()
    print(s.oddCells(2, 2, [[1,1], [0,0]]))

