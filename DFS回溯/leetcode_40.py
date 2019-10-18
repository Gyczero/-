#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 5:37 下午
# @Author  : Frankie
# @File    : leetcode_40.py


from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """

        :param candidates:
        :param target:
        :return:
        """
        candidates.sort()
        res = []
        self._dfs(candidates, [], target, res)
        return res

    def _dfs(self, nums, path, target, res):
        """
        :return:
        """
        value = sum(path)
        if value > target:
            return
        if value == target:
            res.append(path.copy())
            return

        for i in range(len(nums)):
            # 增加判重, 前一个等于后一个，直接跳过
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 设置下一次尝试条件，剪枝
            path.append(nums[i])
            self._dfs(nums[i+1:], path, target, res)
            path.pop(-1)

if __name__ == '__main__':
    print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))