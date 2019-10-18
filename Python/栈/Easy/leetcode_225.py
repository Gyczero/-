#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 1:19 PM
# @Author  : taicheng.guo
# @Site    : 
# @File    : leetcode_225.py
# @Software: PyCharm


from typing import List


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1, self.queue2 = [], []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if len(self.queue1) == 0:
            self.queue1.append(x)
            for i in self.queue2:
                self.queue1.append(self.queue2.pop(0))
        else:
            self.queue2.append(x)
            for i in self.queue1:
                self.queue2.append(self.queue1.pop(0))


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.queue1) == 0:
            return self.queue2.pop(0)
        else:
            return self.queue1.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        if len(self.queue1) == 0:
            return self.queue2[0]
        else:
            return self.queue1[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.queue1) == 0 and len(self.queue2) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()