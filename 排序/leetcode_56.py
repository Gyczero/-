#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-09 22:51
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_56.py
# @Software: PyCharm

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        合并区间 => 区间范围 => 排序
        list最后一个
        :param intervals:
        :return:
        """
        intervals.sort(key=lambda x: x[0])
        new_list = []
        i = 1
        if len(intervals) == 1:
            return intervals
        while i <= len(intervals) - 1:
            tem_list = intervals[i-1]
            # list进行索引，异常判断
            while tem_list[0] <= intervals[i][0] <= tem_list[1]:
                tem_list[1] = max(tem_list[1], intervals[i][1])
                i += 1
                if i > len(intervals)-1:
                    break
            new_list.append(tem_list)
            i += 1

        if i == len(intervals):
            new_list.append(intervals[-1])
        return new_list

    """
    思路比较复杂，增加清晰的思路代码
    """


class Solution2(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if intervals == []:
            return []

        intervals.sort()
        begin = intervals[0][0]
        end = intervals[0][1]
        res = list()
        for i in range(1, len(intervals)):
            if intervals[i][0] > end:
                res.append([begin, end])
                begin = intervals[i][0]
                end = intervals[i][1]
            else:
                if intervals[i][1] > end:
                    end = intervals[i][1]
        res.append([begin, end])
        return res


if __name__ == '__main__':
    print(Solution().merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))

