class Solution:
    def isValid(self, s: str) -> bool:

        # check if char is open bracket if so 
        # we append onto stack
        # if not we check if top of stack matches closed bracket and we pop from stack

# O(n) time
# O(n) space


        stack = []
        mappings = {"}":"{", "]":"[", ")":"("}

        for char in s:
            if char not in mappings:
                stack.append(char)
            
            else:
                if stack and stack[-1] == mappings[char]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False

        