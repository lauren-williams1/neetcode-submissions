class Solution:

    def encode(self, strs: List[str]) -> str:

        result = []
        for string in strs:
            result.append(str(len(string)))
            result.append("!")
            result.append(string)
        return "".join(result)

    def decode(self, s: str) -> List[str]:

        i = 0
        res = []
        # "5!Hello3!you"
        #    i
        #         j

        while i < len(s):
            j = i

            while s[j] != "!":
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res

