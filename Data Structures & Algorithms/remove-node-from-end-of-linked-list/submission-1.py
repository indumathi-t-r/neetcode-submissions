# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = head
        count = 0
        while  tmp!= None:
            count+=1
            tmp = tmp.next
        
        if count == n:
            return head.next
        
        tmp = head
        
        for i in range(1,count-n):
            tmp = tmp.next
        tmp.next = tmp.next.next

        return head
