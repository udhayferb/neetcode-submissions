class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for s1 in s:
            if len(s) == len(t):
                if s1 in t:
                    continue
                else:
                    return False
            else:
                return False
        return True
            
