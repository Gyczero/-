#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 5:38 下午
# @Author  : Frankie
# @File    : leetcode_64.py

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        dp
        都是每次只能向下或者向右移动一步

        dp方程 dp[i][j] = min(dp[i-1][j]+grid[i-1][j], dp[i][j-1]+grid[i][j-1])
        dp初始化
        dp循环
        :param grid:
        :return:
        """

        m = len(grid)
        n = len(grid[0])

        # dp初始化
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = grid[0][0]

        # 在进行list遍历时格外注意，未初始化的部分怎么办
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        # dp循环
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        # 返回结果
        return dp[m-1][n-1]

if __name__ == '__main__':
    print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))


