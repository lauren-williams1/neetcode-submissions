class Solution:
    def isValid(self, s: str) -> bool: 

        # create a stack

        # create dict

        # iterate over string

        # if current char is open bracket we add it to the stack

        # else:

        # check if there is a stack and current char == top of stack

        # if so we pop it otherwise we return false

        # if no stack return true othwerise return false

        stack = []
        mappings = {"}": "{", "]":"[", ")":"("}

        for char in s:
            if char not in mappings:
                stack.append(char)
            else:
                if stack and mappings[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False



        

        

        




        
        
        