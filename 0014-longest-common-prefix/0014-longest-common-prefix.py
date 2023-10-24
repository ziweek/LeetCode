class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        temp = []
        for i,c in enumerate(strs[0]):
            target = [
                c == e_str[i] if i < len(e_str) else False
                for e_str in strs[1:]
            ]
            if False in target:
                break
            else:
                temp.append(c)

        return "".join(temp)