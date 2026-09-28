class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # create out ouput array
        output = [1] * len(nums)

        # prefix = 1
        # for i in range
        # update the prefix and multiply it by the current number in input array

        prefix = 1
        for i in range(len(nums)):
            output[i] *= prefix
            prefix *= nums[i]
        

        # postfix = 1
        # for i in range
        # update postfix and multiply it by the current number
        postfix = 1
        for i in range(len(nums) -1,-1,-1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output


        # return output array

        
        