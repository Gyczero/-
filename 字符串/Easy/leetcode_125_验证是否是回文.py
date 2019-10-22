#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-22 23:13
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_125_验证是否是回文.py
# @Software: PyCharm

from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        双指针法
        a v b : v a b
        :param s:
        :return:
        """
        if s == "":
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            # 找到第一个数字或字符
            while left < len(s) and not s[left].isalnum():
                left += 1
            while right >= 0 and not s[right].isalnum():
                right -= 1

            if left > right:
                return True
            if s[left].upper() != s[right].upper():
                return False
            else:
                left +=1
                right -=1
        return True


