#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-20 00:56
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_120_三角形路径_dp减少空间_改变循环顺序.py
# @Software: PyCharm

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        思路：
        动态规划
        方程：dp[row][column] = min(dp[row-1][column-1], dp[row-1][column+1])

        初始化: 第一行第一列的数据
        两个变量，两重循环
        循环:
        for -> 对于每一行
            for -> 对于每一列
                递推
        return min

        将空间复杂度优化为O(n)
        :param triangle:
        :return:
        """

        dp = [0 for i in range(len(triangle[-1]))]
        dp[0] = triangle[0][0]

        # 注意：如果要求DP减少空间复杂度，改变两个循环的顺序即可，先更新后一个数据，对前一个依赖的数据最后更新
        # 发现数据间的依赖关系，先解决不对其依赖的数据
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])-1, -1, -1):
                left_upper = dp[j-1]+triangle[i][j] if j-1 >= 0 else 9999999
                right_upper = dp[j]+triangle[i][j] if j <= len(triangle[i-1])-1  else 999999
                dp[j] = min(left_upper, right_upper)

        return min(dp)


if __name__ == '__main__':
    print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))


