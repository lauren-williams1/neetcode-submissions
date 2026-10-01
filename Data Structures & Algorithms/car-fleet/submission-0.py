class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        #we need to calc the time it takes for each car to reach the target
        # add that to the stack and then compare each time for each car
        # to see how many fleets there are, return lenth of the stack


        #pair each car's position with it's speed
        pair = [(p,s) for p,s in zip(position, speed)]

        # sort the cars in descending order, closest to the target first
        pair.sort(reverse=True)

        stack = []

        for p,s in pair: 
            stack.append((target-p) / s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


        