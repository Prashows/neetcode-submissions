# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lens =0
        temp = head
        while temp:
            temp = temp.next
            lens +=1

        
        na= lens- n +1
        lend = 1
        curr = head
        prev = None
        
        if   na ==1 :
            return head.next
        while curr:

            if lend == na:
                
                prev.next = curr.next
                break
                
            prev = curr
            curr = curr.next
            lend += 1
        
        return head
    

        