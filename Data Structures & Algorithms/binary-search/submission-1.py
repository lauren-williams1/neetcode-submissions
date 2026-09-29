class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # use a for loop

        # pointers, left and right

        left = 0
        right = len(nums) - 1

        while left <= right:

            #calc the mid point to check and see if its at the middle
            mid = (left + right) //2
            print(mid)

            if nums[mid] == target:
                return mid
            elif target < nums[mid]: # search left side
                right = mid - 1
            else:
                left = mid + 1
        return -1
        