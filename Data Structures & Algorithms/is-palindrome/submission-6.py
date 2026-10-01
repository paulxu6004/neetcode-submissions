class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return False
        
        ri = len(s) - 1
        i = 0     

        
        while i < ri:
            while i < ri and not s[i].isalnum():
                i += 1
            while i < ri and not s[ri].isalnum():
                ri -= 1
            if s[i].lower() != s[ri].lower():
                return False
            i+=1
            ri-=1
        return True
