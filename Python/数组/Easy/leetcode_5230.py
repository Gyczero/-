#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-20 10:41
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_5230.py
# @Software: PyCharm

from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        """
        思路：求delta => 一次循环判断是否等于delta

        Line 15: ZeroDivisionError: division by zero
        横轴纵轴
        :param coordinates:
        :return:
        """
        x_delta = coordinates[1][0] - coordinates[0][0]
        y_delta = coordinates[1][1] - coordinates[0][1]

        for coord in coordinates[2:]:
            x_test = coord[0] - coordinates[0][0]
            y_test = coord[1] - coordinates[0][1]
            if x_delta == 0:
                if x_test == 0:
                    continue
                else:
                    return False
            if y_delta == 0:
                if y_test == 0:
                    continue
                else:
                    return False

            # 这里要除以x_delta，所以注意异常
            if float(x_test/x_delta) != float(y_test/y_delta):
                return False

        return True



