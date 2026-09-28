class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for char in s:
                if char in t:
                    t = t.replace(char,"", 1)
                    s = s.replace(char,"", 1)
                    if len(s) == 0:
                        return True
                else:
                    return False
        else:
            return False

    
