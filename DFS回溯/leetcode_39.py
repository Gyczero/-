#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 4:17 下午
# @Author  : Frankie
# @File    : leetcode_39.py

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        思路：
        选取一些数 => 构成target
        关键词：选取，尝试 => DFS回溯
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
        dfs模块：

        基础数组 nums尝试数组空间
        选择条件, choose哪些东西
        path
        终止条件
        res存储result

        DFS剪枝：一定情况下，不加res
        特别麻烦可以不在res处理，在choose处尝试排序处理，只选择比该值大的值
        一定要注意：DFS中path给res append时，要append list的copy()
        :return:
        """

        # dfs终止条件，剪枝
        value = sum(path)
        if value == target:
            res.append(path.copy())
            return
        if value > target:
            return

        # dfs第一层循环开始，更改循环的条件，变相更改choose
        for i in range(0, len(nums)):
            path.append(nums[i])
            self._dfs(nums[i:], path, target, res)
            path.pop(-1)


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))





