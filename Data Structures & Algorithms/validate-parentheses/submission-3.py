class Solution:
    def isValid(self, s: str) -> bool: 

        #pattern: stack with a dict

        # create our stack
        stack = []

        # create our dictionary
        mappings = {")": "(", "}": "{", "]": "["}


        # need to know when to add bracket to the stack, when to check dict

        for char in s:
        # if current bracket is not in the key of the dict
        # add it to the stack
            if char not in mappings:
                stack.append(char) 


        # check to see if there is a stack and the top of stack matches the current bracket
        # if so we pop the top of stack
            else:
                if stack and mappings[char] == stack[-1]:
                    stack.pop()
                else:
                    return False

        # we keep going

        # if stack is empty return True otherwise return False
        return True if not stack else False

        

        




        
        
        