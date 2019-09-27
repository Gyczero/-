#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-11 00:34
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_20.py
# @Software: PyCharm

from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        """
        注意点：array, apppend, pop
        数组取值 => 做判断是否异常
        :param s:
        :return:
        """
        stack_list = []
        match_dict = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        for i in s:
            if len(stack_list) == 0:
                stack_list.append(i)
                continue

            # 如果是左括，入栈
            if i in match_dict.keys():
                stack_list.append(i)
            # 如果是右括，判断是否匹配
            else:
                # 可能直接是右括的情况
                if len(stack_list) == 0:
                    return False
                if match_dict.get(stack_list[-1]) == i:
                    stack_list.pop(-1)
                    continue
                else:
                    return False

        if len(stack_list) != 0:
            return False
        return True

if __name__ == '__main__':

    print(Solution().isValid("(]"))