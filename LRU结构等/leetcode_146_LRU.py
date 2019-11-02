#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/1 6:38 下午
# @Author  : Frankie
# @File    : leetcode_146_LRU.py


from typing import List


class DoubleLinkNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    """
    重点：
    1、LRU cache中存储的是key对应的Node值,val, node可以被当成存储对象
    2、双向链表设置一个伪头部和伪尾部的结点
    3、LRU cache put时，如果改变了key对应的val，对应node取出，同时更改value，放到链表的最后
    """

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.num = 0
        self.cache = {}
        self.dummy = DoubleLinkNode(-1, -1)
        self.end = DoubleLinkNode(-1, -1)
        self.dummy.next = self.end
        self.end.prev = self.dummy

    def get(self, key: int) -> int:
        """
        get get hash中的值，同时将Hash拆解到尾部
        :param key:
        :return:
        """
        if key not in self.cache:
            return -1
        else:
            # 拆解
            node = self.cache[key]
            val = node.val
            pre_node = node.prev
            next_node = node.next
            pre_node.next = next_node
            next_node.prev = pre_node

            # 放到最后
            end_pre = self.end.prev
            end_pre.next = node
            node.prev = end_pre

            node.next = self.end
            self.end.prev = node
            return val


    def put(self, key: int, value: int) -> None:
        """
        判断是否溢出，
        溢出 => 删除头部，同时将这个接到最后
        未溢出 => 将这个接到最后
        :param key:
        :param value:
        :return:
        """
        if key not in self.cache:
            if self.num >= self.__capacity:
                # pop头部的节点
                head_node = self.dummy.next
                next_node = head_node.next
                self.dummy.next = next_node
                next_node.prev = self.dummy

                # 减少cache，减少num
                self.num -= 1
                self.cache.pop(head_node.key)

            # 将新节点加到尾部之前
            node = DoubleLinkNode(key, value)
            end_pre = self.end.prev

            end_pre.next = node
            node.prev = end_pre

            node.next = self.end
            self.end.prev = node

            # 加cache，加num
            self.cache[key] = node
            self.num += 1

        else:
            # 取出结点，改值，同时放到最后
            node = self.cache[key]
            node.val = value
            pre_node = node.prev
            next_node = node.next
            pre_node.next = next_node
            next_node.prev = pre_node

            # 放到最后
            end_pre = self.end.prev
            end_pre.next = node
            node.prev = end_pre

            node.next = self.end
            self.end.prev = node


        # if self.num >= self.__capacity or key in self.cache:
        #     if key in self.cache:
        #         node = self.cache[key]
        #         node.val = value
        #     else:
        #         # 删除头部
        #         node = self.dummy.next
        #     next_node = node.next
        #     if next_node:
        #         self.dummy.next = next_node
        #         next_node.prev = self.dummy
        #     else:
        #         self.end = self.dummy
        #         self.dummy.next = None
        #
        #     # 删除Hash中的key
        #     self.cache.pop(node.key)
        #
        # # 接到最后
        # node = DoubleLinkNode(key, value)
        # self.end.next = node
        # node.prev = self.end
        # self.end = node
        #
        # self.cache[key] = node
        # self.num += 1




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)