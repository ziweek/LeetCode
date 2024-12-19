# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = []
        
        if not head:
            return True
        
        while head:
            q.append(head.val)
            head = head.next
        print(q)
        
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        return True
        