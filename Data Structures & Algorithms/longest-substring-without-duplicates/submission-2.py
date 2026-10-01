class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        i = 0
        j = 0
        current = set()

        while j < len(s):
            while s[j] in current:
                current.remove(s[i])
                i += 1

            current.add(s[j])
            res = max(res, j - i + 1)
            j += 1

        return res