class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # create dict defaultdict(int)

        # iterate over s, increase count by 1 and add to dict

        # decrement count by 1, as we iterate over t

        # for every value in dict, if values of dict != 0
        # return False

        # otherwise return True


        map = defaultdict(int)

        for char in s:
            map[char] += 1
        
        for char in t:
            map[char] -= 1
        
        for val in map.values():
            if val != 0:
                return False
        return True

                
       