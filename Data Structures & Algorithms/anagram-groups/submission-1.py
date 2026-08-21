class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)
        

        for string in strs:
            newMap = [0] * 26

            for char in string:
                newMap[ord(char) - ord('a')] += 1
            result[tuple(newMap)].append(string)
    
        
        return list(result.values())