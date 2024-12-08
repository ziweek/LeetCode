# 1. 확인할 점
# array > 빈 배열이 있는지 (X), 중복된 요소가 있는지 (O), 
# integer > 양수 or 0 or 음수 (O)
# return > 항상 솔루션 있는지 (O)

# 2. 검증 케이스 살펴보기
# [2,7,11,15] 9 > [0,1]
# [3,2,4] 6 > [1,2]
# [3,3] 6 > [0,1]
# [-2,0,1,4] 2

# 3. 개념으로 작성
# 반복 i,e (nums)
#   반복 j,e (nums)
#       조건 (i+j = target)
#           조건 (i != j)
#             반환 [i,j] 

# 4. 코드로 작성

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # nums = [3,3]
        # target = 6
        
        for i,e_i in enumerate(nums):
            for j,e_j in enumerate(nums):
                if e_i + e_j == target:
                    if i != j:
                        # print(f"i: {i}, j: {j}")
                        return [i, j]
        
        
#         for i in range(len(nums)):
#             for j in range(len(nums) - 1):
#                 if nums[i] + nums[j+1] == target:
#                     return [i, j+1]
#                 return [0,0]

        