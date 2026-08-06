class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        #use stack to add numbers to it
        # then when we get to an operator we perform calc from previous two numbers we pop

        # save each calc as result


        stack = []

        for item in tokens:
            if item == "+":
                stack.append(stack.pop() + stack.pop())
            
            elif item == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            
            elif item == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append( a * b)
            elif item == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b/a)))
            else:
                stack.append(int(item))
        return stack[-1]


        


        

        

        


    
    









        