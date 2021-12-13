class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
        
#将传入的数组转化为链表
def create_linkedlist(nums):
    head = ListNode(nums[0])
    cur = head
    for i in range(1, len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    return head


def reverse_linkedlist(head):
    if not head:
        return None
    rev = None
    # ph = head
    # while ph:
    #     rev, rev.next, ph = ph ,rev, ph.next
    while head:
        next = head.next
        head.next = rev
        rev = head
        head = next
    return rev

def transTolist(head):
    res = []
    if not head:
        return None
    while head:
        res.append(head.val)
        head = head.next
    return res

def mergeTwoLinkedlist(head1:ListNode, head2:ListNode):
    if head1 == None and head2 == None:
        return None
    if head1 != None  and head2 == None:
        return head1
    if head1 == None  and head2 != None:
        return head2
    elif head1.val < head2.val:
            head1.next = mergeTwoLinkedlist(head1.next, head2)
            return head1
    elif head1.val >= head2.val:
            head2.next = mergeTwoLinkedlist(head1, head2.next)
            return head2

def sort(head):
    dummy1 = ListNode(head.val)
    dummy2 = ListNode(0)
    cur1 = dummy1
    cur2 = dummy2
    index = 0
    while head:
        head = head.next
        index += 1
        if index % 2 != 0:
            cur2= ListNode(head)
            cur2 = cur2.next
        else:
            cur1.next = ListNode(head)
            cur1 = cur1.next
    reverse_linkedlist(dummy2.next)
    return mergeTwoLinkedlist(dummy2, dummy1)

head = [4, 5, 6, 7,8, 9, 10]
head1 = create_linkedlist(head)
head2 = reverse_linkedlist(head1)
#print(create_linkedlist(head))
#print(reverse_linkedlist(head1))
#print(transTolist(head2))
lt2 = [1, 7, 2,4,  5,3, 6 ]

headx = create_linkedlist(lt2)

print(sort(headx))



# headx = create_linkedlist(lt2)
# print(sort(headx))

