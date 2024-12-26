class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        b = bisect_left(nums, target)
        print(b)
        return -1 if b >= len(nums) or nums[b] != target else b
        