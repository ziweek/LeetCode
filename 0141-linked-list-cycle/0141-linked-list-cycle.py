# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        tail = head
        # tail_next = tail.next
        nums = []
        while tail != None:
            if tail not in nums:
                nums.append(tail)
            else:
                return True
            tail = tail.next
            

                
        
