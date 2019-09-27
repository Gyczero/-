#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-22 10:58
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_5198.py
# @Software: PyCharm

from typing import List

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        """
        思路:
        1、减少数存储的空间，用0/1表示
        2、使用空间换时间

        正确思路：
        1、直观的优化措施就是看能不能将时间复杂度降低到O（n），即只在丑数上花时间，而不在非丑数上浪费时间
        2、剑指offer上给的思路很好，用O（n）的辅助空间来得到O(n)的时间复杂度
        3、每一个丑数必然是由1~N个整数同丑数的乘积得到的, 每次乘积后，选择最小的那个作为新的丑数

        Binary search:
        https://leetcode.com/problems/ugly-number-iii/discuss/387539/cpp-Binary-Search-with-picture-and-Binary-Search-Template
        思路：
        1、交集求所有元素
        2、二分查找
        :param n:
        :param a:
        :param b:
        :param c:
        :return:
        """
        import math
        # 0、时间复杂度2*10**9
        lo = 1
        hi = 2*10**9

        # 计算最小公倍数
        ab = a*b//math.gcd(a, b)
        bc = b*c//math.gcd(b, c)
        ac = a*c//math.gcd(a, c)
        abc = a*bc//math.gcd(a, bc)

        # 二分查找的循环
        while(lo < hi):
            mid = lo+(hi-lo)//2
            index = mid//a + mid//b + mid//c - mid//ab - mid//bc - mid//ac + mid//abc
            if index < n:
                lo = mid+1
            else:
                hi = mid
        return lo



        # 1、时间复杂度10**18
        # alist = []
        # for i in range(10**18):
        #     if (i%a == 0) or (i%b ==0) or (i%c==0):
        #         alist.append(1)
        #         if sum(alist) == n+1:
        #             return len(alist)-1
        #     else:
        #         alist.append(0)

        # 2、时间复杂度O(n)
        # # 每一个丑数因子记录一个值
        # min_num = 0
        # a_w, b_w, c_w = 1,1,1
        #
        # # 这样时间复杂度就是O(n)
        # for i in range(n):
        #     a_num = a_w * a
        #     b_num = b_w * b
        #     c_num = c_w * c
        #
        #     min_num = min(a_num, b_num, c_num)
        #     if min_num == a_num:
        #         a_w+=1
        #     if min_num == b_num:
        #         b_w+=1
        #     if min_num == c_num:
        #         c_w+=1
        #
        # return min_num


if __name__ == '__main__':
    print(Solution().nthUglyNumber(4,2,3,4))
