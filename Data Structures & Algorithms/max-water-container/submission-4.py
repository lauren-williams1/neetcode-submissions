class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # create two pointers
        # track maxArea of the water

        # iterate over the array
        # calculate the max area

        # if height of left < right:
        # move pointers respectively
        # return maxArea


        maxArea = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            maxArea = max(maxArea, (right -left) * min(heights[left], (heights[right])))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea
        