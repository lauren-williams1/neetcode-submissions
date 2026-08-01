class Solution:
    def isValid(self, s: str) -> bool: 

        # create a stack
        # create dict to map open and closing brackets

        # iterate over each item in string

        # determine if item is in a dict key or not
        # if not we push it onto the stack

        # otherwise if it is a closing bracket, compare with the top of the stack
        # if it is we pop top of stack

        #otherwise we return False

        # end, we check to see if stack is empty return True otherwise return False

        stack = []
        mappings = {"}": "{", "]": "[", ")": "("}


        for item in s:
            if item not in mappings:
                stack.append(item)
            else:
                if stack and mappings[item] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False

        




        
        
        