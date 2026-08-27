class Solution:
    def trap(self, height: List[int]) -> int:

        # create two pointers
        # track left and right max as tallest walls seen

        # while left < right:
        # if leftmax < rightmax

        # process left and move left up

        # else process right and move right down

        # return total trapped water

        # edge case, check if there is any height
        if not height:
            return 0
        
        # create left and right pointers
        left, right = 0, len(height) - 1
        # create max height for left and right
        leftMax, rightMax = height[left], height[right]
        # create var to store final result
        result = 0

        # while left < right, to make sure they don't cross as we itearte over array
        while left<right:
            # if the left
            if leftMax < rightMax:
                left += 1
                leftMax = max(height[left], leftMax)
                result += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(height[right], rightMax)
                result += rightMax - height[right]
        return result

        
        