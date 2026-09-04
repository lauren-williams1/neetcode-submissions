class Solution:
    def isValid(self, s: str) -> bool: 

        # create dict

        # create stack

        # iterate over the string

        # if char is not in the stack. we will add it to the stack

        # otherwise if there is a stack compare top of stack with value of the current char we are on
        
        map = {"}":"{", "]":"[", ")":"("}
        stack = []

        for char in s:
            if char in map:
                if stack and stack[-1] == map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False


        



        

        

        




        
        
        