#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-06 23:37
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_46_回溯算法.py
# @Software: PyCharm


from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        思路:
        1、循环遍历，增加到数组 => 时间复杂度高
        2、回溯算法：permutation，枚举每个位置可以放哪些数字
        基本思想：
        DFS => 深度优先遍历 + 状态重置 + 剪枝
        DFS结构：
        1、存储变量
        >> 需要遍历的数据
        > nums: 需要填充的数组  【原始数据】
        > res：排列结果变量  【DFS路径信息保存】
        >> 用什么来区别不同的分支状态，用什么来记录数据: used记录状态, path记录数据
        > used: 当前的位置有哪些数字可以放 【DFS填充选择】
        > path: 已有path中包含的数据   【DFS路径信息】

        2、框架
        > 递归终止条件
            如果已经得到的path和nums长度相同
        > 递归过程:
            1、遍历首次的第一种情况
            2、根据第一种情况，更改状态，used,path
            3、递归从第一种情况向下遍历
            4、第一种情况结束，回溯，状态变回之前的状态
        :param nums:
        :return:
        """
        if not nums:
            return []
        res = []
        used = [False for i in nums]
        self.__dfs(nums, [], used, res)
        return res


    def __dfs(self, nums, path, used, res):
        """
        dfs递归函数
        :param nums: 需要遍历的数组
        :param index:
        :param pre:
        :param used:
        :param res:
        :return:
        """
        # 递归终止条件，终止时，增加该path到res
        if len(path) == len(nums):
            # 【特别注意】：因为path是一个list，在这里append是append这个list的一个引用，当list发生变化时，res里引用的数据也发生变化
            # 因为list中只有值，这里浅拷贝即可
            res.append(path.copy())
            return

        # 递归过程
        for i in range(len(nums)):
            # 判断数字是否使用过
            if not used[i]:

                used[i] = True
                path.append(nums[i])
                # dfs子树
                self.__dfs(nums, path, used, res)

                # 【遍历一分支后回溯到原来的状态】
                used[i] = False
                path.pop()



if __name__ == '__main__':
    Solution().permute([1,2,3])

