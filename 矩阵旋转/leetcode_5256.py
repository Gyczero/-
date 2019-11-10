#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-10 10:41
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_5256.py
# @Software: PyCharm

from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        """
        二进制矩阵压缩
        思路:
        1、终止 upper,low > len(colsum)
        2、第一行长度为len(colsum) while upper i >= len(colsum) return None且colusm > 0，赋值为1，colsum - 1, colsum=0, i+=1,
        4、第二行同样 while lower i=0
        5、遗忘点：优先减去2
        :param upper:
        :param lower:
        :param colsum:
        :return:
        """
        col_num = len(colsum)
        if upper > col_num or lower > col_num or upper+lower != sum(colsum):
            return []

        line1 = [0 for _ in range(col_num)]
        line2 = [0 for _ in range(col_num)]

        # 统计colsum中2的数量
        two_index = []
        for i in range(col_num):
            if colsum[i] == 2:
                two_index.append(i)
            elif colsum[i] > 2:
                return []

        while len(two_index) != 0:
            if upper <= 0:
                return []
            index = two_index.pop()
            colsum[index] -= 1
            line1[index] = 1
            upper -= 1
        index = 0
        while upper > 0:
            if index >= col_num:
                return []
            if colsum[index] > 0 and line1[index] == 0:
                line1[index] = 1
                colsum[index] -= 1
                upper -= 1
            index += 1

        index = 0
        while lower > 0:
            if index >= col_num:
                return []
            if colsum[index] > 0 and line2[index] == 0:
                line2[index] = 1
                colsum[index] -= 1
                lower -= 1
            index+=1
        return [line1, line2]

if __name__ == '__main__':
    s = Solution()
    print(s.reconstructMatrix(4, 2, [1,2,1,2,0]))