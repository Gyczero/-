#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 10:12 上午
# @Author  : Frankie
# @File    : leetcode_1114_按序打印.py


from typing import List, Callable
import threading

"""
考点：多线程的阻塞
1、while循环法：
方法：用某些方法卡住执行顺序，然后不断监控目标，直到目标符合条件时才跳出当前断点继续执行后续语句。
缺点：没法像threading模块那样很好的监控线程，所以大概率会超时

2、信号量法：信号量为0时进行阻塞
threading 信号量有两个方法：acquire和release
1、信号量是由操作系统管理的一种抽象数据类型，用于在多线程中同步对共享资源的使用。
本质上说，信号量是一个内部数据，用于标明当前的共享资源可以有多少并发读取。
2、Acquire：内置计数器-1, 直到为0的时候阻塞，每当线程想要读取关联了信号量的共享资源时，必须调用 acquire() ，
此操作减少信号量的内部变量, 如果此变量的值非负，那么分配该资源的权限。如果是负值，那么线程被挂起，直到有其他的线程释放资源。
3、Release：内置计数器+1，并让某个线程的acquire()从阻塞变为不阻塞，当线程不再需要该共享资源，必须通过release() 释放。
这样，信号量的内部变量增加，在信号量等待队列中排在最前面的线程会拿到共享资源的权限。

3、锁同步：Lock锁对象法，互斥锁
线程的竞争条件：
当两个或以上对共享内存的操作发生在并发线程中，并且至少有一个可以改变数据，又没有同步机制的条件下，就会产生竞争条件，可能会导致执行无效代码、bug、或异常行为。

锁的两个方法：
休息室
acquire() 占用，
release() 释放
可能会造成死锁的产生。
"""

"""
锁同步Lock
"""
class Foo:
    def __init__(self):
        self.s1 = threading.Lock()
        self.s1.acquire()
        self.s2 = threading.Lock()
        self.s2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.s1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self.s1.acquire()
        printSecond()
        self.s2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        self.s2.acquire()
        printThird()


# """
# 信号量法：多线程对共享资源的使用
# """
# class Foo:
#     def __init__(self):
#         self.s1 = threading.Semaphore(0)
#         self.s2 = threading.Semaphore(0)
#
#     def first(self, printFirst: 'Callable[[], None]') -> None:
#         # printFirst() outputs "first". Do not change or remove this line.
#         printFirst()
#         self.s1.release()
#
#     def second(self, printSecond: 'Callable[[], None]') -> None:
#         # printSecond() outputs "second". Do not change or remove this line.
#         self.s1.acquire()
#         printSecond()
#         self.s2.release()
#
#         def third(self, printThird: 'Callable[[], None]') -> None:
#             # printThird() outputs "third". Do not change or remove this line.
#             self.s2.acquire()
#             printThird()