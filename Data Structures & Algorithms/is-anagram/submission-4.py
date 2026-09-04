class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        map = defaultdict(int)

        for char in s:
            map[char] += 1
        
        for char in t:
            map[char] -= 1
        
        for val in map.values():
            if val != 0:
                return False
        return True
        