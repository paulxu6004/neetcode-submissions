class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        prev = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in prev:
                prev[sorted_s].append(s)
            else:
                prev[sorted_s] = [s]
                
        return list(prev.values())