class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)

        for string in strs:
            map = [0] * 26

            for char in string:
                # count frequency of each char and store as the key
                map[ord(char) - ord('a')] += 1

                # store each word for that key
            result[tuple(map)].append(string)
        
        # return list of values of the dict
        return list(result.values())

        