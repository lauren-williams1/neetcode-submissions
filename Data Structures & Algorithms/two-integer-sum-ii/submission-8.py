class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        # create two pointers
        
        # for loop

        # while loop

        # calc total
         # return left + 1, right + 1

        # if total > 0, move right down 1

        # if total < 0, move left up 1

        left = 0
        right = len(numbers) - 1

        while left < right:

            total = numbers[left] + numbers[right]

            if total > target:
                right -= 1

            elif total < target:
                left += 1
            else:
                return [left + 1, right + 1]
                
        return []
            

        