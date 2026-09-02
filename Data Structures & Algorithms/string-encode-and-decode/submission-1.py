class Solution:

    def encode(self, strs: List[str]) -> str:
        #iterate over each string and store the total amount of characters before
        # string and before string starts you can put a nonalpha char to determine
        # when the string starts
        result = []
        for string in strs:
            result.append(str(len(string)))
            result.append("#")
            result.append(string)
        return "".join(result)

    def decode(self, s: str) -> List[str]:

        # iterate over string
        # pointer so we know when to start decoding the string

        i = 0
        result = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j +1
            j = i + length
            result.append(s[i:j])
            i = j
        return result


        

            




        



