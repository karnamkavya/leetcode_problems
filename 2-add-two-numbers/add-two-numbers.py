# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        carry=0
        while l1 and l2:
            v=l1.val+l2.val+carry
            carry=v//10
            v=v%10
            curr.next=ListNode(v)
            l1=l1.next
            l2=l2.next
            curr=curr.next
        while l1:
            if carry==1:
                v=l1.val+carry
                carry=v//10
                v=v%10
                curr.next=ListNode(v)
            else:
                curr.next=l1
            l1=l1.next
            curr=curr.next
        while l2:
            if carry==1:
                v=l2.val+carry
                carry=v//10
                v=v%10
                curr.next=ListNode(v)
            else:
                curr.next=l2
            l2=l2.next
            curr=curr.next  
        if carry==1:
            curr.next=ListNode(carry)      
        return dummy.next