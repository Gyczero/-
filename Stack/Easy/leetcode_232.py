#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-12 21:09
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_232.py
# @Software: PyCharm


class MyQueue:
    """
    注意点：for i in range(数组): 数组.pop(i) 要重点考虑数组的长度变化
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.assist_stack = []
        self.nums = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        self.nums+=1

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        for i in range(self.nums):
            self.assist_stack.append(self.stack.pop(-1))

        first_value = self.assist_stack.pop(-1)
        self.nums-=1
        for i in range(self.nums):
            self.stack.append(self.assist_stack.pop(-1))
        return first_value

    def peek(self) -> int:
        """
        Get the front element.
        """
        for i in range(self.nums):
            self.assist_stack.append(self.stack.pop(-1))

        first_value = self.assist_stack[-1]

        for i in range(self.nums):
            self.stack.append(self.assist_stack.pop(-1))

        return first_value


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.nums == 0:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()