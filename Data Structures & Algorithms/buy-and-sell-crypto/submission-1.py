class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        i = 1
        nl = len(prices)
        mn = prices[0]
        while i < nl:
            v = prices[i]
            mn = min(mn, v)
            m = max(m, v-mn)
            i+=1
        return m