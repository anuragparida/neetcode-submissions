class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for l in s:
            d[l] = d.get(l, 0) + 1
        for l in t:
            if l not in d or d[l] < 1:
                return False
            d[l] -= 1
        for l in d:
            if d[l] != 0:
                return False
        return True