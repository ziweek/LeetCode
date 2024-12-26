class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        result = 0
        
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] >= target:
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        b = result
        
        # b = bisect_left(nums, target)
        print(b)
        return -1 if b >= len(nums) or nums[b] != target else b
        