#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-03 23:20
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_66.py
# @Software: PyCharm

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        注意点：
        1、int和str的相互转换
        2、map的使用
        :param digits:
        :return:
        """
        number = str(int("".join(map(str, digits))) + 1)
        return [int(i) for i in number]


if __name__ == '__main__':

    s = Solution()
    print(s.plusOne([1,2,3]))


