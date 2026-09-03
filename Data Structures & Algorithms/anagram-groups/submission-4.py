class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)

        for string in strs:
            map = [0] * 26

            for char in string:
                map[ord(char) - ord('a')] += 1
            result[tuple(map)].append(string)
        return list(result.values())