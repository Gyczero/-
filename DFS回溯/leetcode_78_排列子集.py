#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 11:38 上午
# @Author  : Frankie
# @File    : leetcode_78_排列子集.py

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        思路：DFS

        可选数组
        choose过程
        path记录 res总结结果
        终止条件 target
        :param nums:
        :return:
        """
        # 数组排序
        nums.sort()
        res = []
        self._dfs(nums, [], res)
        return res


    def _dfs(self, nums, path, res):
        """
        :return:
        """
        # 一定要注意copy()
        res.append(path.copy())
        if len(nums) == 0:
            return

        for i in range(len(nums)):
            path.append(nums[i])
            self._dfs(nums[i+1:], path, res)
            path.pop(-1)







