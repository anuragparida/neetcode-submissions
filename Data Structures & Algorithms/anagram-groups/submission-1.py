class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            sorteds = "".join(sorted(s))
            if sorteds in d:
                d[sorteds].append(s)
            else:
                d[sorteds] = [s]
        fl = [d[x] for x in d]
        # print(fl)
        return fl