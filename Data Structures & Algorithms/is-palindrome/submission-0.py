class Solution:
    def isPalindrome(self, s: str) -> bool:
        sf = ""
        for l in s:
            if l.isalnum():
                sf += l.lower()
        return sf == ''.join(reversed(sf))