# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head1 = l1
        head2 = l2
        newnode = ListNode(0,None)
        data = newnode
        carry = 0
        while head1 or head2 or carry:
            
            head11 = head1.val if head1 else 0
            head22 = head2.val if head2 else 0

            curr = head11 + head22 + carry
            carry = curr // 10
            curr = curr%10
            

            data.next = ListNode(curr)
            data = data.next
            head1 = head1.next if head1 else 0
            head2 = head2.next if head2 else 0
        
        return newnode.next