class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #initialize result array
        # cerate prefix var

        # first pass-from left to the right

        # for each index, set current number = prefix
        # update the prefix *= nums[i]

        # create postfix var
        # second pass from right to left


        res = [1]  * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

        

            


        

