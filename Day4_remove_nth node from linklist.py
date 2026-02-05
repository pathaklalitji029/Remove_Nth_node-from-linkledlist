# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        #we make fast and slow pionter that start with head of the linklist 
        p1=head
        p2=head

        #traverse the p2 till n node given

        for i in range(n):
            p2=p2.next
        #check the p2 is null after n node traverse then head nodr tp we delete 
        #it is the edge case for removing the nth node
        if p2==None:
            head=head.next
            return head

        #here after edge case fails then this iterate works to remove nth node

        while p2.next!=None:
            p1=p1.next
            p2=p2.next
        p1.next=p1.next.next
        return head

# Helper functions
def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

head=create_linked_list([1,2,3,4,5])
n=2

obj=Solution()
new_head=obj.removeNthFromEnd(head,n)

print(print_linked_list(new_head))
