class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        stack = []
        braks = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for char in s:
            if char in braks: 
                if len(stack) < 1:
                    return False

                elif stack[-1] == braks[char]:
                    stack.pop(-1)

                elif stack[-1] != braks[char]:
                    return False
            
            else: 
                stack.append(char)



        if len(stack) == 0:
            return True   
        return False
        
        
        


        