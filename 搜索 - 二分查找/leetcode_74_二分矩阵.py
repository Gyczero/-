#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 7:59 下午
# @Author  : Frankie
# @File    : leetcode_74_二分矩阵.py


from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        高效算法 -> 矩阵中是否存在一个目标值 o(m*n)以下
        1、从左 -> 右升序，二分
        2、矩阵整体递增
        O(logN)
        二分查找模板

        low, high, mid
        （判断是否有序）
        target同mid比较，归约到两边
        while low < high:
            mid
            if low , high

        矩阵这个使用list表示元素的index太麻烦了
        => 思考一维数组表示形式

        注意：！！！ 如何将二维矩阵同一维list进行坐标互换
        row = idx // n
        col = idx % n
        接下来，可以按照二分查找的来做

        总结：
        1、在进行二分查找时，首先考虑将业务条件抽象成模型（矩阵 => List下标的形式），整体代码量和思路简单
        2、注意二分查找中的 left <= right 的等号！！！
        :param matrix:
        :param target:
        :return:
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_row = mid // len(matrix[0])
            mid_col = mid % (len(matrix[0]))
            mid_value = matrix[mid_row][mid_col]

            if mid_value == target:
                return True
            elif target < mid_value:
                right = mid - 1
            elif target > mid_value:
                left = mid + 1
        return False

        # row_index = len(matrix)-1
        # col_index = len(matrix[0])-1
        #
        # low = [0, 0]
        # high = [row_index, col_index]
        #
        # while (low[0] < high[0]) or (low[0] == high[0] and low[1] <= high[1]):
        #     # 矩阵mid怎么取
        #     numbers = ((high[0]-low[0]) * len(matrix[0]) + (high[1] - low[1])) // 2
        #     row_change = numbers // len(matrix[0])
        #     col_change = numbers - row_change * len(matrix[0])
        #     mid = [low[0] + row_change, low[1] + col_change]
        #     mid_value = matrix[mid[0]][mid[1]]
        #     if target == mid_value:
        #         return True
        #     elif target > mid_value:
        #         # 更改low
        #         if mid[1] + 1 > col_index:
        #             low[0], low[1] = mid[0]+1, 0
        #         else:
        #             low[0], low[1] = mid[0], mid[1]+1
        #     elif target < mid_value:
        #         # 更改high
        #         if mid[1] - 1 < 0:
        #             high[0], high[1] = mid[0] - 1, col_index
        #         else:
        #             high[0], high[1] = mid[0], mid[1]-1
        # return False


if __name__ == '__main__':
    print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))



