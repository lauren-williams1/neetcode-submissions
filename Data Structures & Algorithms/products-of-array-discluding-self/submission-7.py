class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # create an array of 1s

        # iterate over nums get the product of everything to left of each number
        # and store in new array in correct position

        # iterate over nums from backwards the front and get product of everything to the 
        # right of each number, return the new array

        # use prefix = 1 and postfix = 1
        
        #output = [1,1,1,1]
        # nums = [1,2,4,6]

        # iteration 1: prefix = 1
   
        """

        # multiply the prefix and product to left of each number and save as prefix
        # continue on in the loo
"""

        output = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            output[i] *= prefix
            prefix *= nums[i]

        
        postfix = 1
        for i in range(len(nums) -1,-1,-1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output

