# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    
        dummy = ListNode(0,head)
        
        prevgroup = dummy
        while True:
            kth = self.kthitem(prevgroup,k)
            if not kth :
                break
            nextgroup = kth.next

            prev =   kth.next
            current  = prevgroup.next
            while  current != nextgroup:
                temp = current.next 
                current.next = prev
                prev = current
                
                current =  temp
            temp = prevgroup.next
            prevgroup.next = kth
            prevgroup = temp
        return dummy.next


    def kthitem(self, curr, k):
            while curr and k>0:
                curr = curr.next
                k -= 1
            return curr



       
             
