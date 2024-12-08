# 1. 확인할 내용
# integer > positive or 0 or negative
# always solvable? > 

# 2. 추가 검증케이스
# 121 > true
# -121 > true
# 10 > false

# 3. 

class Solution:
    def isPalindrome(self, x: int) -> bool:
    
        
        if x < 0:
            temp = -1
            x = x * temp
        else:
            temp = 1
        li_x = list(str(x))
        li_x.reverse()
        num_output = int(''.join(li_x)) * temp
        if num_output == x:
            return True
        return False
        