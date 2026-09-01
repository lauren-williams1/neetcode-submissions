class Solution:
    def isPalindrome(self, s: str) -> bool:

        # transofrm string to remove whitespace and alphanum chars

        # create two pointers

        # iterate over the string
        # compare left and right
        # if they don't equal each other return false,
        # otherwise we move pointers respectively

        s = "".join(c.lower() for c in s if c.isalnum())
        left = 0
        right = len(s) - 1

        for c in s:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        return True




       
        