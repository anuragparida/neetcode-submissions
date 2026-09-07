class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nl = len(nums)
        p = [1] * nl
        s = [1] * nl
        for i in range(1, nl):
            if i == 1:
                p[i] = nums[i-1]
            else:
                p[i] = nums[i-1] * p[i-1]
        for i in range(nl-2, -1, -1):
            if i == nl - 2:
                s[i] = nums[i+1]
            else:
                s[i] = nums[i+1] * s[i+1]
        ret = []
        for i in range(nl):
            if i == 0:
                x = s[i]
            elif i == nl - 1:
                x = p[i]
            else:
                x = p[i] * s[i]
            ret.append(x)
        return ret