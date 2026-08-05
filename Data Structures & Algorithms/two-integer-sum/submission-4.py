class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        #create dictionary

        # iterate over array

        # calculate complement

        # check if complement in dictionary

        # if not add it to the dictionary

        # return []


        map = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in map:
                return [map[complement], i]
            map[nums[i]] = i
        
        return []
        