#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 6:40 下午
# @Author  : Frankie
# @File    : leetcode_48_顺时针旋转.py

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        观察矩阵
        难点：原地
        Python批量赋值
        矩阵90度旋转 = 矩阵转置 + 翻转
        矩阵的转置，从0-len, 内部循环从i-len
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 矩阵转置后再进行翻转
        for row in matrix:
            row.reverse()
