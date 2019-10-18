#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 4:54 下午
# @Author  : Frankie
# @File    : leetcode_77.py


from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        思路：
        组合尝试 => 回溯DFS
        :param n:
        :param k:
        :return:
        """
        nums = range(1, n+1)
        res = []
        self._dfs(nums, [], k, res)
        return res

    def _dfs(self, nums, path, limit, res):
        """

        初始数组
        choose条件
        终止条件
        path记录
        res.append

        :return:
        """
        if len(path) == limit:
            res.append(path.copy())
            return

        # 针对DFS进行优化
        # 这个1000ms+
        # for i in range(0, len(nums)):
        # 考虑不允许重复，剪枝的终止条件不应该是后边的数，而应该这个，156ms
        for i in range(0, min(len(nums)-(limit-len(path))+2, len(nums))):
            path.append(nums[i])
            self._dfs(nums[i+1:], path, limit, res)
            path.pop(-1)


if __name__ == '__main__':
    print(Solution().combine(4, 2))