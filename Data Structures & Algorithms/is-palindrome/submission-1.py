class Solution:
    def isPalindrome(self, s: str) -> bool:

        # change string

        # create pointers

        # iterate over string

        # check if left and right are equaled to each other
        # if so continue and move pointers, if not return False


        s = "".join(char.lower() for char in s if char.isalnum())

        left = 0
        right = len(s) - 1

        for char in s:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        return True

        