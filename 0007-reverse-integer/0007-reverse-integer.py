# 1. 확인할 점
# 정수 -> 양수, 0, 음수
# 항상 return 존재 X -> return 0

# 2. 검증 케이스
# 123 -> 321
# -123 -> -321
# 120 -> 021
# 155 -> 551
 
# 3. 개념 구상

# 4. 코드로 작성

class Solution:
    def reverse(self, x: int) -> int:
        # x = 1_534_236_469
        if x >= 0:
            temp = 1
        else:
            temp = -1
            x = x * temp
            
        li_x = list(str(x))
        li_x.reverse()
        output = int("".join(li_x)) * temp
        
        if -2**31 <= output <= (2**31)-1:
            print(f"x:{x * temp}, output:{output}")
            return output
        else:
            print(f"x:{x * temp}, output:{0}")
            return 0
    
        
        