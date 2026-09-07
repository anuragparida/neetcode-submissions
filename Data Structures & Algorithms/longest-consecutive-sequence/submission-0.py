class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        m = 0
        def howmanystarting(x):
            j = 1
            while x + 1 in ns:
                j += 1
                x += 1
            return j
        for x in ns:
            if x-1 in ns:
                continue
            else:
                nlx = howmanystarting(x)
                m = max(m, nlx)


        return m
