class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        #keeps track of days in decreasing order from bottom to top that 
        # are waiting for a warmer temperature

        #we scan forward, when we find a temperature higher than thte one on top of the stack, we discovred the next warmer day for that earlier day.

        # pop it and compute the difference in days, and continue

        stack = []
        #create list of 0s
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t,i))
        return res


        