#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 8:06 下午
# @Author  : Frankie
# @File    : leetcode_95_不同的二叉搜索树.py

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def numTrees(self, n: int) -> int:
        """
        二叉搜索树：
        中节点大于左子树节点，小于右子树节点
        思路：动态规划
        1、为什么能想到DP而不是递归？？
        > 为什么用DP
        给定一个有序序列 1 ... n，为了根据序列构建一棵二叉搜索树。
        我们可以遍历每个数字 i，将该数字作为树根，1 ... (i-1) 序列将成为左子树，(i+1) ... n 序列将成为右子树。
        于是，我们可以递归地从子序列构建子树。
        在上述方法中，由于根各自不同，每棵二叉树都保证是独特的。
        可见，问题可以分解成规模较小的子问题。
        因此，我们可以存储并复用子问题的解，而不是递归的（也重复的）解决这些子问题，这就是动态规划法。
        > DP和递归的区别？
        > DP: 也是将一个原问题分解为若干个规模较小的子问题，递归的求解这些子问题，然后合并子问题的解得到原问题的解。
        > 1.区别在于这些子问题会有重叠，一个子问题在求解后，可能会再次求解，
        于是我们想到将这些子问题的解存储起来，当下次再次求解这个子问题时，直接拿过来就是。
        > 2.即用动态规划能解决的问题分治策略肯定能解决，只是运行时间长了。
        因此，分治策略一般用来解决子问题相互对立的问题，称为标准分治，而动态规划用来解决子问题重叠的问题

        DP推导:
        G(n)为1~n的二叉搜索树数量，f(i)为以i为根的二叉搜索树数量
        G(n) = f1 + f2 .. + fn
        而f(i)左边为1~i-1,右边为i+1~n，左边可以形成的二叉搜索树数量为G(i-1)；右边为G(n-i)
        所以f(i) = G(i-1) * G(n-i)
        所以G(n) = f1 + f2 + ... + fn
        所以G(n) = G(0)*G(n-1) + G(1)*G(n-2) + ... + G(n-1)*G(0)
        所以dp公式 => 循环
        :param n:
        :return:
        """

        dp = [0 for _ in range(n+1)]
        # 0代表
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            tem = 0
            for j in range(1, i+1):
                tem += dp[j-1]*dp[i-j]
            dp[i] = tem
        return dp[-1]





