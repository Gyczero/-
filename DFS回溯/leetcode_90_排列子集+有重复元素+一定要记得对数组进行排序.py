#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 5:10 下午
# @Author  : Frankie
# @File    : leetcode_90_排列子集+有重复元素+一定要记得对数组进行排序.py

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        思路: DFS
        ！！！ 在做重复元素进行DFS时，如果需要去重重复元素，一定要记得将数组进行排序排序排序！！！
        :param nums:
        :return:
        """
        nums.sort()
        res = []
        self._dfs(nums, [], res)
        return res



    def _dfs(self, nums, path, res):
        """
        nums
        choose
        path res
        终止条件target
        :return:
        """
        res.append(path.copy())
        if len(nums) == 0:
            return

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self._dfs(nums[i+1:], path, res)
            path.pop(-1)




