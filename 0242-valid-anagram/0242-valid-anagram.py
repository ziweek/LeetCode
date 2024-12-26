class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # print(sorted(s))
        # print(sorted(t))
        # print(sorted(s) == sorted(t))
        return sorted(s) == sorted(t)
        