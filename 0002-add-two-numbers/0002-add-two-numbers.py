# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 함수 (뒤집기)
# 함수 (합치기)
# 함수 (더하기)
# 함수 (뒤집기)
# 함수 (나누기)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_value = 0        
        num = 1
        while l1:
            l1_value += l1.val*num
            l1 = l1.next
            num *= 10
        
        l2_value = 0
        num = 1
        while l2:
            l2_value += l2.val*num
            l2 = l2.next
            num *= 10
        
        out_value = l1_value + l2_value
        print(l1_value, l2_value, out_value)
        
        header = None
        linked_list = None
        for c in str(out_value):
            if not header:
                header = ListNode(int(c))
                linked_list = header
            else:
                curNode = ListNode(int(c), linked_list)
                linked_list = curNode
                
                
        return linked_list