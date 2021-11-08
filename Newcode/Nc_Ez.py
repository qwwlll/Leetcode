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

    def jumpFloor(self, number):
        # write code here]
        #斐波那契数列 变式
        a,b=1,2
        if number==1:
            return 1
        for _ in range(number-2):
            a,b=b,a+b 
        return b

    def merge(self , A, m, B, n):
            # write code here
            #整合两个有序数组
        for i in range (n):
            A[m+i] = B[i]
        A.sort()     
        print(A)
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        #连续字数组最大的和
        dp = [i for i in array]
        for i in range(1,len(array)):
            dp[i] = max(dp[i-1]+array[i],array[i])
        return max(dp)