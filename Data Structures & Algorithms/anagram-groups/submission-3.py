class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)

        for word in strs:
            map = [0] * 26

            for char in word:
                map[ord(char) - ord('a')] += 1
            result[tuple(map)].append(word)
        return list(result.values())


        