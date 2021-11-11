#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
## 翻转链表

def reverse(self, head):
    if not head or not head.next:
        return head
    pre = None
    while head:
        next = head.next  # 保存当前头节点的下一个节点
        head.next = pre  # 将当前头节点的下一个节点指向 “上一个节点”，实现反转
        pre = head  # 将当前头节点设置 “上一个节点”
        head = next  # 将保存的下一个节点设置 “头节点”
    return pre
## other way
def revisedList(self, pHead):
    if pHead == None:
        return None
    head = pHead
    rev  = None
    while head :
        rev, rev.next, head = head, rev, head.next
    return rev

## 是否有环：
## 双指针 当t.next.next = s, 意味着快的指针已经转了一圈过来和他相等， 证明有环。
def hasCycle(self , head: ListNode) -> bool:
    if head == None:
        return False
    s = head
    t = head
    while t and t.next:
        t = t.next.next
        s = s.next
        if t == s:
            return True
    return False

## 寻找环的入口//Find the entry:
## 同双指针，测到环后，双指针停止，快指针指向head， 慢指针继续，当再次相遇， 快指针到达入口。
def EntryNodeOfLoop(self, pHead):
    # write code here
    fast, slow = pHead, pHead
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:    
            break
    if not fast or not fast.next:
        return None
    fast = pHead
    while fast != slow:
        fast = fast.next
        slow = slow.next
            
    return fast

##  合并两个有序链表 升序方式（递归）
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    elif not l2:
        return l1
    elif l1.val <= l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2

## 删除倒数第n个node // delete the late number n node
##（双指针，快满差别n位，引入dummynode in order to print the head）

def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

    dummynode = ListNode(0, head)
    first = head
    second = dummynode
    for i in range(n):
        first = first.next
    while first:
        first = first.next
        second = second.next
            
    second.next = second.next.next
    return dummynode.next

## other way(计算链表长度然后删除）
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        dummy = ListNode(0, head)
        length = getLength(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next


## 链表的中间node // middle node of the linkedList
##（ 双指针，快x2 慢x1）
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return None
        s, t  = head , head 
        while t and t.next:
            s = s.next
            t = t.next.next
            
        return s

## 两链表数相加

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = curr = ListNode()
    carry = 0
    while l1 or l2:
        if l1:
            x = l1.val
        else:
            x = 0
        if l2:
            y = l2.val
        else:
            y = 0
        all = x + y + carry
        curr.next = ListNode(all % 10)
        curr = curr.next
        carry = all // 10
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    if carry:
        curr.next = (ListNode(carry))
    return dummy.next     


    ## 单链表排序
class Solution:
    def sortInList(self , head: ListNode) -> ListNode:
        # write code here
        temp = []   ### 造list 
        temp.append(head.val)
        while head.next:
            head = head.next
            temp.append(head.val) ## 将链表存入list // sort
        temp.sort()
        res = ListNode(-1)### 新建链表， 放入
        tp = res
        for i in temp:
            t = ListNode(i)
            tp.next = t
            tp = tp.next
        return res.next

### 判断回文
class Solution:
    def isPail(self, head) -> bool:
        #链表为空，直接返回true
        if head is None:
            return True

        #找到链表的中点
        middle_point = self.middle_point(head)
        second_start = self.reverse_list(middle_point.next)

        #判断前半部分和后半部分是否相等
        result = True
        first = head
        second = second_start
        while result and second is not None:
            if first.val != second.val:
                result = False
            first = first.next
            second = second.next

        #还原链表并返回结果
        middle_point.next = self.reverse_list(second_start)
        return result

    #快慢指针寻找中点
    def middle_point(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    #翻转链表
    def reverse_list(self, head):
        previous = None
        current = head
        while current:
            previous, previous.next, current = current, previous, current.next
            
        return previous
