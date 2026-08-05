class Solution:
    def isPalindrome(self, s: str) -> bool:

        # re-do s

        # create poiters

        # for loop

        # if left and right are not equaled to each other, return False

        # otherwise move left and right

        # otherwise return True

        s = "".join(char.lower() for char in s if char.isalnum())

        left = 0
        right = len(s) - 1

        for char in s:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True


        