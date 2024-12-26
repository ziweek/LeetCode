class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # s_replaced = s.lower().replace(" ", "").replace(",", "").replace(".", "").replace(":", "")
        
        # s_replaced = [e if e.isalpha() else "" for e in s.lower().replace(" ", "")]
        # print(s_replaced)
        s_replaced = []
        for e in s.lower().replace(" ", ""):
            if e.isalnum():
                s_replaced.append(e)
        
        if len(s_replaced) <= 1:
            return True
        
        # print(s_replaced)
        i_start = 0
        i_end = len(s_replaced)-1 - i_start
        # print(i_start, i_end)
        while i_start <= i_end:
            if s_replaced[i_start] == s_replaced[i_end]:
                i_start += 1
                i_end -= 1
                if len(s_replaced[i_start:i_end+1]) <= 1:
                    return True
            else:
                return False
        return False
            
        