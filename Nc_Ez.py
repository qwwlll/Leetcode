# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        #翻转链表
        p = None
        head = pHead
        while head:
            temp = head.next
            head.next, p , head =  p, head, temp
        return p

    def hasCycle(self , head: ListNode) -> bool:
        #是否有环，双指针
        if not head:
            return False
        s = head
        t = head
        while t and t.next:
            t = t.next.next
            s = s.next
            if t == s:
                return True
        return False