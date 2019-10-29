#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 6:01 下午
# @Author  : Frankie
# @File    : leetcode_22_括号生成.py

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        :param n:
        :return:
        """
        if n == 0:
            return []
        res = []
        self._dfs(n, "", res, 0, 0)
        return res

    def _dfs(self, n, path, res, left_num, right_num):
        """
        nums, res, path, choose
        :return:
        """
        if len(path) == 2*n:
            res.append(path)
            return

        chooses = []
        if left_num < n:
            chooses.append('(')
        if right_num < left_num:
            chooses.append(')')

        for i in chooses:
            path += i
            if i == '(':
                self._dfs(n, path, res, left_num+1, right_num)
            else:
                self._dfs(n, path, res, left_num, right_num+1)
            path = path[:-1]

if __name__ == '__main__':
    print(Solution().generateParenthesis(3))

