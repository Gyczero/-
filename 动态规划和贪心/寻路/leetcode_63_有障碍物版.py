#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 4:40 下午
# @Author  : Frankie
# @File    : leetcode_63_有障碍物版.py


from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        思路:
        动态规划 + 障碍物
        dp[m][n] =
        if dp[m-1][n]障碍物 => 0
        if dp[m][n-1]障碍物 => 0
        :param obstacleGrid:
        :return:
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]

        # dp初始化, 如果有障碍物，后边都为0
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                # 当数组为0时，特殊处理
                for i in range(j, n):
                    dp[0][i] = 0
                break
            dp[0][j] = 1

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                # 接下来的行数都=0
                for j in range(i, m):
                    dp[i][0] = 0
                break
            dp[i][0] = 1

        # 两层循环
        for i in range(1, m):
            for j in range(1, n):
                left_value = 0 if obstacleGrid[i-1][j] == 1 else dp[i-1][j]
                right_value = 0 if obstacleGrid[i][j-1] == 1 else dp[i][j-1]
                dp[i][j] = left_value + right_value if obstacleGrid[i][j] != 1 else 0

        return dp[m-1][n-1]

if __name__ == '__main__':
    print(Solution().uniquePathsWithObstacles([[1]]))