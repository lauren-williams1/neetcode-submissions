class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # sliding window-longest, while condition is invalid


        # create set
        # create left pointer
        # create n
        # create final length of new array


        # iterate over array
        # while char in set"
        # remove left and move window up 1
        # add character to the window
        # return length of longest substring


        charSet = set()
        left = 0
        n = len(s)
        maxLength = 0

        for right in range (len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        return maxLength


        

        


        

