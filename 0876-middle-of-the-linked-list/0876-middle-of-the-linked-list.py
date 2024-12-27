# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = []
        counter = 0
        while head != None:
            result.append(head)
            head = head.next
            counter += 1

        return result[counter // 2]

        