class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # create stac
        # iterate over stack witha for loop
        # total = 0

        stack = []
        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif char == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            elif char == "/":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(float((b)/a)))
            else:
                stack.append(int(char))
        return stack[0]


        

        


        


        

        

        


    
    









        