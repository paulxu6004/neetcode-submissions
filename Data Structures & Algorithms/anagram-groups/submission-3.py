class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freqs = {}

        for s in strs:
            freq = [0] * 26
            for i in range(len(s)):
                freq[ord(s[i]) - ord('a')] += 1
            
            if tuple(freq) in freqs:
                freqs[tuple(freq)].append(s)
            else:
                freqs[tuple(freq)] = [s]

        res = []

        for f in freqs:
            res.append(freqs[f])
        
        return res