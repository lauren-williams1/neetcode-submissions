class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        charSet = set()
        n = len(s)
        result = 0

        for right in range(n):

            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            result = max(result, right - left + 1)
        return result

