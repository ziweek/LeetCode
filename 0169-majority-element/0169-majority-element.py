class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = Counter(nums).items()
        return sorted(num_dict, key=lambda x: x[1], reverse=True)[0][0]