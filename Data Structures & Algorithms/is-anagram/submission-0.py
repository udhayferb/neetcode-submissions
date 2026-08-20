class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for s1 in s:
            if s1 in t:
                continue
            else:
                return False
        return True
            
