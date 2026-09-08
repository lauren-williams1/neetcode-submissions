class Solution:
    def isValid(self, s: str) -> bool:

        # DS: stack + hashmap
        # can determine if open and closed brackets match
        # add open brackets onto stack and see if it matches the key in hashamp of closing brackets

        # when we add on to stack-push open bracket
        # pop when we find a match

        map = {"}":"{", ")":"(", "]":"["}
        stack = []

        for char in s:
            if char not in map.keys():
                stack.append(char)
            else:
                print(stack)
                if stack and stack[-1] == map[char]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False
        