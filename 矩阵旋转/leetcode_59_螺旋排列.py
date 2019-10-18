#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 1:11 下午
# @Author  : Frankie
# @File    : leetcode_59_螺旋排列.py

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        顺时针螺旋排列的正方形矩阵
        :param n:
        :return:
        """
        matrix = [[0 for i in range(n)] for i in range(n)]
        i = 1
        delta = 0
        max_index = n-1
        limit = n**2

        while i <= limit:
            for j in range(delta, max_index-delta+1, 1):
                matrix[delta][j] = i
                i += 1
            if i > limit:
                break

            for j in range(delta+1, max_index-delta+1, 1):
                matrix[j][max_index-delta] = i
                i += 1
            if i > limit:
                break

            for j in range(max_index-delta-1, delta-1, -1):
                matrix[max_index-delta][j] = i
                i += 1
            if i > limit:
                break

            for j in range(max_index-delta-1, delta, -1):
                matrix[j][delta] = i
                i += 1
            if i > limit:
                break

            delta += 1
        return matrix


if __name__ == '__main__':
    print(Solution().generateMatrix(3))


