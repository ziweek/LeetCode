class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
#         s_replaced = []
#         for e in s.lower().replace(" ", ""):
#             if e.isalnum():
#                 s_replaced.append(e)
        
#         if len(s_replaced) <= 1:
#             return True
    
#         i_start = 0
#         i_end = len(s_replaced)-1 - i_start
#         while i_start <= i_end:
#             if s_replaced[i_start] == s_replaced[i_end]:
#                 i_start += 1
#                 i_end -= 1
#                 if len(s_replaced[i_start:i_end+1]) <= 1:
#                     return True
#             else:
#                 return False
#         return False
        s_replaced = []
        for e in s.lower().replace(" ", ""):
            if e.isalnum():
                s_replaced.append(e)
        return s_replaced == s_replaced[::-1]
                
            
        