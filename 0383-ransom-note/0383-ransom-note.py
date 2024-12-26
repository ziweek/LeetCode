class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote_map = Counter(ransomNote)
        print(ransomNote_map)
            
        magazine_map = Counter(magazine)
        print(magazine_map)
        
        for e,num in ransomNote_map.items():
            if e not in magazine_map.keys():
                return False
            if num > magazine_map[e]:
                return False
        return True
            
        