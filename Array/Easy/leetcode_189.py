#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 1:01 PM
# @Author  : taicheng.guo
# @Site    : 
# @File    : leetcode_189.py
# @Software: PyCharm


from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        注意点：
        1、数组越界
        """

        if not nums:
            pass

        for i in range(k):
            nums.insert(0, nums[-1])
            nums.pop(-1)



if __name__ == '__main__':

    s = Solution()
    test_list = [-1,-100,3,99]
    s.rotate(test_list, k=3)
    print(test_list)