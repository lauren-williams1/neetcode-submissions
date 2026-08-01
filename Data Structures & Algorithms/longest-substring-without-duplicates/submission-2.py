class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # maxChars = 0
        # left = 0
        # charSet = set()


        # right in range()

        # if char is not in set:
        # add the char to the set
        # update the maxLength of substring

        # while, condition has to be invalid for us to expand the window
        # char is in the set:
        # we remove the left
        # move window up one and add the right

        # return maxLEngth


        maxLength = 0
        left = 0
        charSet = set()

        # for right in range(len(s)):
        #     if s[right] not in charSet:
        #         charSet.add(s[right])
        #         maxLength = max(maxLength, right - left + 1)
        #     else:
        #         while s[right] in charSet:
        #             charSet.remove(s[left])
        #             left += 1
        #         charSet.add(s[right])
        # return maxLength


        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        return maxLength


        

