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
        
        # brute force Approach
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []
         
        # HashMap Approach
        numToIndex = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in numToIndex:
                return [numToIndex[complement], i]
            numToIndex[num] = i
        return []
                                                   
        

        