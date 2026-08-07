class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        """
        use a stack tp lee[ tracl pf daus that are still waiting for
        normal temp

        instead of iterating over array multiple times as we traverse through the array

        use a stack to find higher temp than the current temp, pop it, compute the difference 
        and continue
        """

        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t,i))

        return res

