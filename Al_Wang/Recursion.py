## NC 68 跳台阶
##1.问题的解可以分解为几个子问题的解。何为子问题？就是数据规模更小的问题。
##2.问题与子问题，除了数据规模不同，求解思路完全一样
##3.存在递归终止条件
##（这个问题， number太大导致超时） O（2^n）
class Solution: 
    def jumpFloor(self, number):
        # write code here
        so = 0
        if number == 0: 
            so = 1 
            return so
        elif number == 1: 
            so = 1 
            return so
        elif number == 2: 
            so = 2 
            return so
        
        return self.jumpFloor(number - 1 ) + self.jumpFloor(number - 2)

##other way
##申请两个变量
class Solution:
    def jumpFloor(self, number):
        # write code here
        a, b = 1, 1
        if number <= 1:
            return 1
        for _ in range (1, number):
            a, b  = b, a + b 
        return b




## leetcode 50 pow(x,n):
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        def pox(x:float, n:int):
            if n == 0:
                return 1.0
            ans = self.myPow(x, n//2)
            if n % 2 == 0:

                return ans * ans
            else:
                return ans * ans * x
        if n > 0:
            return pox(x,n)
        else:
            return 1.0/pox(x,-n)



##leetcode 203 从链表删除对应的val
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        H = ListNode(-1)
        H.next = head
        cur = H
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return H.next