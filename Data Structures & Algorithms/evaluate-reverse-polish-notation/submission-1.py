class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # string of numbers and operators
        # use stack to keep track of numbers, when we get to operator we perform math and continue


        # create a stack
        stack = []

        for item in tokens:

            if item == "+":
                stack.append(stack.pop() + stack.pop())
            
            elif item == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif item == "*":
                stack.append(stack.pop() * stack.pop())
            elif item == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b/a)))
            else:
                stack.append(int(item))
        return stack[-1]

        # iterate over the list of strings

        # if the first number in string is a number
        # add it to the stack

        # need to know what to do when there is a number and when there is an operator

        # if item in string == "+":
        # remove two numbers and add them together


         # if item in string == "-":
        # remove two numbers and add them together

 # if item in string == "*":
        # remove two numbers and add them together


 # if item in string == "/":
        # remove two numbers and add them together


        

        

        


    
    









        