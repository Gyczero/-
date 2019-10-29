#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 11:16 上午
# @Author  : Frankie
# @File    : leetcode_23_合并排序链表.py


from typing import List
# Python导入堆
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        思路：
        1、遍历每个list => list同list合并 => 双指针O(m+n) * O(N)
        2、堆：完全二叉树
        3、堆的构建、增、
        堆的删除是针对于根结点而言，删除后，将二叉树的最后一个节点替换到根结点，然后自顶向下，递归调整
        堆排序：时间复杂度O(NlogN)
        大根堆：每一个节点的值不小于孩子节点值的树
        小根堆：每一个节点的值不大于孩子节点值的树
        一、Python怎么实现一个小顶堆
        heapq
        ans = []
        heapq.heapqpush(ans, 1) 把ans看做一个小顶堆，把1push到这个小顶堆中
        heapq.headpify 变成堆
        heap.heappop 取最小的
        heapq.nsmallest  nlargest 最大，最小
        二、Python实现一个大顶堆
        数据进堆的时候把所有的数据取相反数~

        优先队列：
        不再遵循先进先出的规则：
        最大优先队列，无论入队顺序，当前最大的元素优先出队。
        最小优先队列，无论入队顺序，当前最小的元素优先出队。
        满足以上需求的话，最坏情况下需要时间复杂度为O(N)

        最大堆来实现最大优先队列，每一次入队操作就是堆的插入操作，每一次出队操作就是删除堆顶节点。
        优先队列的入队和出队时间复杂度O(logN)

        时间复杂度: O(logk * N)
        :param lists:
        :return:
        """
        heap = []
        for index in range(len(lists)):
            if lists[index]:
                # 最小堆插入元素 (heap, (堆中元素, 链表的索引index))
                heapq.heappush(heap, (lists[index].val, index))

        dummy = ListNode(-1)
        cur = dummy
        while heap:
            # 最小堆取最小的元素 heappop(heap)
            _, index = heapq.heappop(heap)
            head = lists[index]

            cur.next = head
            cur = cur.next

            if head.next:
                heapq.heappush(heap, (head.next.val, index))
                lists[index] = head.next
                head.next = None
        return dummy.next


        # 时间复杂度: kN
        # if len(lists) == 0:
        #     return None
        #
        # if len(lists) == 1:
        #     return lists[0]
        # dummy = ListNode(-1)
        # dummy.next = lists[0]
        # pointer1 = dummy.next
        # pre = dummy
        # for alist in lists[1:]:
        #     pointer2 = alist
        #     while pointer1 is not None and pointer2 is not None:
        #         if pointer1.val >= pointer2.val:
        #             pre.next = pointer2
        #             pointer2 = pointer2.next
        #             pre = pre.next
        #         else:
        #             pre.next = pointer1
        #             pointer1 = pointer1.next
        #             pre = pre.next
        #
        #     if not pointer1:
        #         pre.next = pointer2
        #     if not pointer2:
        #         pre.next = pointer1
        #
        #     pointer1 = dummy.next
        #     pre = dummy
        # return dummy.next





