class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # sliding window: length of window

        # create start of window
        # create length of substring
        
        # iterate over string
        
        # create hashmap

        # count maxChar count

        # while window - maxCount >=k:
        # remove left char, move window up 1
        # calc length of substring

        # return substring

        left = 0
        maxCount = 0
        char_count = {}
        result = 0

        for right in range(len(s)):

            char_count[s[right]] = 1 + char_count.get(s[right], 0)

            maxCount = max(maxCount, char_count[s[right]])

            while (right-left+1) - maxCount > k:
                char_count[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result


       
        