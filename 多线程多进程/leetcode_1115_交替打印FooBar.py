#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 11:57 上午
# @Author  : Frankie
# @File    : leetcode_1115_交替打印FooBar.py

from typing import List, Callable
import threading


"""
生产者和消费者问题：foo是生产者，bar是消费者，
要先生产才能被消费, 并且商品缓冲区上限为1
"""
"""
按照生产者消费者、信号量的机制来看，商品缓冲区上限为1
"""

class FooBar:
    def __init__(self, n):
        self.n = n
        self.s1 = threading.Semaphore(1)
        self.s2 = threading.Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.s1.acquire()
            printFoo()
            self.s2.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.s2.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.s1.release()


"""
按照mutex互斥锁的机制来看
"""
# class FooBar:
#     def __init__(self, n):
#         self.n = n
#         self.s1 = threading.Lock()
#         self.s2 = threading.Lock()
#         self.s2.acquire()
#
#     def foo(self, printFoo: 'Callable[[], None]') -> None:
#         for i in range(self.n):
#             # printFoo() outputs "foo". Do not change or remove this line.
#             self.s1.acquire()
#             printFoo()
#             self.s2.release()
#
#     def bar(self, printBar: 'Callable[[], None]') -> None:
#
#         for i in range(self.n):
#             self.s2.acquire()
#             # printBar() outputs "bar". Do not change or remove this line.
#             printBar()
#             self.s1.release()

