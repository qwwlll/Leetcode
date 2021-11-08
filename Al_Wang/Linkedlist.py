#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
## 翻转链表
def reviseList(self, pHead):
    if pHead == None:
            return None
    head = pHead
    rev = None
    nxt = None
    while head :
        nxt = head.next
        head.next = rev
        rev = head
        head = nxt
    return rev

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
