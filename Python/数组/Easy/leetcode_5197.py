#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-22 10:37
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_5197.py
# @Software: PyCharm

from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        """
        思路:
        1、数组 => 排序
        2、遍历，如果等于最小，加入结果list
        3、如果小于最小，结果list清空，增加该值，最小值更新
        :param arr:
        :return:
        """

        min_value = 9999999
        return_list = []

        # 排序
        arr.sort(reverse=False)

        # 遍历
        for i in range(len(arr)-1):
            abs_value = abs(arr[i] - arr[i+1])
            if abs_value < min_value:
                min_value = abs_value
                return_list = []
                return_list.append([arr[i], arr[i+1]])

            elif abs_value == min_value:
                return_list.append([arr[i], arr[i+1]])

        return return_list

if __name__ == '__main__':
    print()



