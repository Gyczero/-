#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 9:46 PM
# @Author  : taicheng.guo
# @Site    : 
# @File    : leetcode_268.py
# @Software: PyCharm

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        数组 => 等差数列 => 求和
        :param nums:
        :return:
        """
        # 常数空间 + 线性时间复杂度
        max_value = len(nums)
        full_sum = ((0+max_value) * (max_value+1)) / 2
        nums_sum = sum(nums)
        return int(full_sum - nums_sum)

        # 等差数列，最小到最大求和 - sum(nums) = 空缺的值
        # tem = [i for i in range(max(nums)+1) if i not in nums]
        # if len(tem) == 0:
        #     return -1
        # else:
        #     return tem[0]


if __name__ == '__main__':

    s = Solution()
    print(s.missingNumber([9,6,4,2,3,5,7,0,1]))