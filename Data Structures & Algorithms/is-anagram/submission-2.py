class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        count1 = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        
        for char1 in t:
            if char1 in count1:
                count1[char1] += 1
            else:
                count1[char1] = 1
        for i in count:
            if count.get(i) == count1.get(i):
                continue
            else:
                return False
        return True

