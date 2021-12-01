### leetcode26: 删除有序数组中的重复项
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 1
        n = len(nums)
        for i in range(n-1):
            if nums[i] != nums[i+1]:
                nums[index] = nums[i+1]
                index += 1
        return index

###jzII 032:有效的变位词
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s ==t :
            return False
        def countingl(s:str):
            dic = {}
            for i in s:
                dic[i] = s.count(i)
            return dic
        n =countingl(s)
        m =countingl(t)
        return n == m

### leetcode 160 链表相交
#  Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return 
        a = headA
        b = headB
        while a != b :
            if a:
                a = a.next
            else:
                a =headB
            if b:
                b = b.next
            else:
                b = headA
        return a     
