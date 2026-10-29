class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        seen = set(nums)
        total_length = 0

        
        # check for each number in the set
        for num in seen:
            # check if the number is not in the set
            if (num - 1) not in seen:
                # incerase total length of set to 1
                length = 1
                # while the current number plus 1 is in the set, increase total length
                # find the max value between longest length found and total_length
                while  (num + length) in seen: 
                    length += 1
                total_length = max(length, total_length)
        
        return total_length





        

      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        #use a data structure to keep track of elements that are consecuvite by 1
        # end return length of that array 

        # look at first number okay its 2
        # check if this is the smallest number we have seen so far
        # look at next one and see if it is equaled to the previous number + 1
        # if not we continue in the array
        # otherwise we add number to the new array

        # convert input list to a set for O(1) lookip

        result - 0
        store = set(nums)

        for num in nums:
            streak

        seen = set()

        for i in range(len(nums)):
            if i >= nums[i-1]:
                continue
            
            elif nums[i+1] == nums[i] + 1:
                print(seen.add(nums[i]))
        return len(seen)



        