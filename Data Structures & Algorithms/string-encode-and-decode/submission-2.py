class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ""
        for s in strs:
            r += str(len(s)) + "$" + s
        return r
    def decode(self, s: str) -> List[str]:
        r = []
        if s == "":
            return []
        n = 0 #index
        while n < len(s):
            nx = s[n:].find("$") + n
            d = int(s[n:nx])
            n = nx + 1
            r.append(s[n:n+d])
            n += d
        return r