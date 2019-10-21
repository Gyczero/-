#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-21 21:52
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_17_电话号码字母组合.py
# @Software: PyCharm

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        dfs
        :param digits:
        :return:
        """
        digits = [i for i in digits if i != 1]

        if not digits:
            return []

        dict = {
            '2':['a', 'b', 'c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z']
        }
        res = []
        self._dfs(digits, '' , res, dict)
        return res


    def _dfs(self, nums, path, res, dict):
        """
        choose条件
        终止条件
        :return:
        """
        if len(nums) == 0:
            res.append(path)
            return

        for i in dict[nums[0]]:
            path += i
            self._dfs(nums[1:], path, res, dict)
            path = path[:-1]

if __name__ == '__main__':
    print(Solution().letterCombinations("23"))


