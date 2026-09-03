class Solution:
    def trap(self, height: List[int]) -> int:

        # optimal two pointer solution
        # total var

        # need left and right pointers
        # height of the max for right and left
        # we iterate over the array and then decide what side to process
        # once we do we process left/right, moving pointer, find the max height for that side
        # to determine to find how much water there is trapped between the bars
        # once we do that we return total

        left = 0
        right = len(height) - 1

        leftMax, rightMax = height[left], height[right]

        total = 0
        while left < right:

            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                total += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                total += rightMax - height[right]
        return total










                
                