class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # optimal way: stack
        # add two numbers on to the stack, once we get to an operation 
        # pop the two numbres and add product onto the stack
        # continue throughout the array

        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b/a)))

            else:
                stack.append(int(token))
        return stack[-1]






        