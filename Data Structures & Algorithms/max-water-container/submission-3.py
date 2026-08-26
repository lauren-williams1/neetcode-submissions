class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # 2 pointers
        # keep track of max area of container
        # create two pointers

        # iterate over the list of heights

        # calculate the max area

        # while left < right:

        # move the left up 1

        # otehrweise we move the right down 1

        # return maxarea


        left = 0
        right = len(heights)- 1
        maxArea = 0

        while left < right:
            maxArea = max(maxArea, (right- left) * min(heights[left], heights[right]))

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea




        

        
        