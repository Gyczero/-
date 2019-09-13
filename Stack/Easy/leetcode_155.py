#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-11 23:10
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_155.py
# @Software: PyCharm

from typing import List

class MinStack:
    """
    注意点：空间换时间，要求时间常数内
    =>
    借助另一个栈来存储当前栈中的最小值，
    注意点：：：【小于等于】
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__stack_list = []
        self.__min_stack = []

    def push(self, x: int) -> None:
        if not self.__min_stack or (x <= self.__min_stack[-1]):
            self.__min_stack.append(x)
        self.__stack_list.append(x)

    def pop(self) -> None:
        value = self.__stack_list.pop(-1)
        if value == self.__min_stack[-1]:
            self.__min_stack.pop(-1)

    def top(self) -> int:
        return self.__stack_list[-1]

    def getMin(self) -> int:
        return self.__min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()