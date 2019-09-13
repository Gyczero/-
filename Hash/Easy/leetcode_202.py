#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-13 16:58
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_202.py
# @Software: PyCharm

class Solution:
    def isHappy(self, n: int) -> bool:
        """
        思路：
        1、如果一个数是非快乐数，那么一定会无限循环下去
        2、记录之前的数，如果得到的数在之前List中，那么这个数就是非快乐数
        :param n:
        :return:
        """

        before_num = []
        n_sum = 0
        while(n_sum != 1):
            n_sum = 0
            for i in str(n):
                n_sum += int(i) ** 2

            if n_sum in before_num:
                return False
            before_num.append(n_sum)
            n = n_sum
        return True

if __name__ == '__main__':
    print(Solution().isHappy(19))