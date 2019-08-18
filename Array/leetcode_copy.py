#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-18 22:03
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_copy.py
# @Software: PyCharm

from typing import List
import copy

class Solutions:

    def copy_test(self, m:List):

        # 直接赋值，对象的引用
        direct_assign = m
        direct_assign.append(999)

        # 浅拷贝，对象拷贝，List中元素操作与copy后的无关，
        # 对象的子对象还是引用
        shadow_copy = copy.copy(m)
        method_copy = m.copy()

        # 深拷贝
        deepcopy = copy.deepcopy(m)

        m.append(111)
        m[4].append('test')

        print("direct_assign = {}".format(direct_assign))
        print("shadow_copy = {}".format(shadow_copy))
        print("method_copy = {}".format(method_copy))
        print("deep_copy = {}".format(deepcopy))

if __name__ == '__main__':
    a = [1, 2, 3, 4, ['a', 'b']]

    print("raw a = {}".format(a))

    Solutions().copy_test(a)

    print("source list = {}".format(a))

