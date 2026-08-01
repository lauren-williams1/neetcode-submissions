class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        # create a dictionary
        map = {}

        # iterate over number
        for i in range(len(nums)):

        # calc the complement
            complement = target - nums[i]

        # if complement in dict
            if complement in map:

        # return it with current number
                return [map[complement], i]

        #otherwise add number to dict
            map[nums[i]] = i


        # return []
        return []

        
        
        
        