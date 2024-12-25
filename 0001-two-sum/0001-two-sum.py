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
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
            
        
        # for i_1, e_1 in enumerate(nums):
        #     for i_2, e_2 in enumerate(nums):
        #         if i_1 != i_2:
        #             if e_1 + e_2 == target:
        #                 return [i_1, i_2]
        
        
                        
        
        # for i_1, e_1 in enumerate(nums):
        #     for i_2, e_2 in enumerate(nums):
        #         if e_1 + e_2 == target:
        #             if i_1 != i_2:
        #                 return [i_1, i_2]

#         for i, n in enumerate(nums):
#             complement = target - n
            
#             if complement in nums:
#                 return [nums.index(n), nums[i+1:].index(complement) + (i+1)]

                
        
        # nums = [3,3]
        # target = 6
        
        # for i,e_i in enumerate(nums):
        #     for j,e_j in enumerate(nums):
        #         if e_i + e_j == target:
        #             if i != j:
        #                 return [i, j]
        
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         print(i, j)
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
                
#         hashMap = {nums[idx]: idx for idx in range(len(nums))}
#         print(hashMap)
        
#         for idx in range(len(nums)):
#             complement = target - nums[idx]
#             if hashmap.
                                                   
        

        