#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 6:06 下午
# @Author  : Frankie
# @File    : leetcode_73_矩阵置零.py


from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        直接解决：维护一个O(mn)的包含0 index的matrix
        改进方法：
        维护一个O(m)的list，存储0的行
        维护一个O(n)的list，存储0的列

        继续优化空间复杂度：常数级
        思考方式:
        这两个list能不能放到矩阵中？
        能 => 需要针对放置0的位置设置标志位，判断第一行第一列是否有0
        """

        # 1、O(m+n)复杂度
        # zero_row = []
        # zero_column = []
        #
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == 0:
        #             zero_row.append(i)
        #             zero_column.append(j)
        #
        # for i in list(set(zero_row)):
        #     matrix[i] = [0 for i in range(len(matrix[0]))]
        #
        # for j in list(set(zero_column)):
        #     for i in range(len(matrix)):
        #         matrix[i][j] = 0

        # 2、常数级时间复杂度
        row = len(matrix)
        col = len(matrix[0])
        row0_flag = False
        col0_flag = False
        # 找第一行是否有0
        for j in range(col):
            if matrix[0][j] == 0:
                row0_flag = True
                break
        # 第一列是否有0
        for i in range(row):
            if matrix[i][0] == 0:
                col0_flag = True
                break

        # 把第一行或者第一列作为 标志位
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        # print(matrix)
        # 置0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row0_flag:
            for j in range(col):
                matrix[0][j] = 0
        if col0_flag:
            for i in range(row):
                matrix[i][0] = 0






