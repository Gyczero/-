#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-20 10:53
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_5231.py
# @Software: PyCharm

from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        """
        注意：操作数组的方式：
        1、从前往后/从后往前遍历
        2、从前，二次迭代
        3、从前，之前迭代的
        判断是否值得加入
        Python String if "" in ""
        :param folder:
        :return:
        """
        res = set()
        folder.sort()
        def check(f):
            s = f.split('/')[1:]
            tmp = ''
            for i in s:
                tmp += ('/' + i)
                if tmp in res:
                    return False
            return True
        for f in folder:
            if check(f):
                res.add(f)
        return res

if __name__ == '__main__':
    # Python sort排序，
    # 按照期望中的排序方式
    s = ['a', 'abc', 'ab', 'ca', 'cab']
    s.sort()
    print(s)