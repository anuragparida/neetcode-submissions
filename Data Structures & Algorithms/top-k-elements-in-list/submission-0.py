class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nd = Counter(nums)
        return [k for k, v in sorted(nd.items(), key=lambda item: item[1], reverse=True)][:k]
        