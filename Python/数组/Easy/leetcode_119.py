#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 21:49
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_119.py
# @Software: PyCharm

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        优化算法 => 空间复杂度O(k)，只保存上一次的结果
        :param rowIndex:
        :return:
        """
        result_list = []
        for i in range(1, rowIndex+2):
            row_list = []
            for j in range(i):
                if (j==0) or (j==i-1):
                    row_list.append(1)
                else:
                    row_list.append(result_list[j-1] + result_list[j])
            result_list = row_list
        return result_list

if __name__ == '__main__':

    s = Solution()
    print(s.getRow(3))
