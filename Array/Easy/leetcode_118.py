#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 21:30
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_118.py
# @Software: PyCharm

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        第一个和最后一个都为1
        x[i][j] = x[i-1][j-1] + x[i-1][j]
        :param numRows:
        :return:
        """
        result_list = []
        for i in range(1, numRows+1):
            row_list = []
            for j in range(i):
                if (j==0) or (j==i-1):
                    row_list.append(1)
                else:
                    value = result_list[i-2][j-1] + result_list[i-2][j]
                    row_list.append(value)
            result_list.append(row_list)

        return result_list

if __name__ == '__main__':

    s = Solution()
    print(s.generate(5))






