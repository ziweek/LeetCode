# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # for i in range(1, n+1):
        #     # print(i, isBadVersion(i))
        #     if isBadVersion(i):
        #         return i
        
        
        low = 0
        high = n
        
        while low < high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        print(low, mid, high)
        return low

        
        
        
#         l = 0
#         r = n

#         while l < r:

#             mid = (l + r) // 2

#             if isBadVersion(mid):
#                 r = mid
#             else:
#                 l = mid + 1

#         return l