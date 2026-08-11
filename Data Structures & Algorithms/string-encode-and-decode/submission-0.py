class Solution:

    def encode(self, strs: List[str]) -> str:
        # store in one large list-length of string, a delimiter and string itself
        # so that you can  determine how to decode the string back to it's original form

        res = []
        for string in strs:
            res.append(str(len(string)))
            res.append("#")
            res.append(string)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        # have pointer to start to iterate over string
        # determine length of string based on number in encoded string
        # this will determine how far we move our pointer
        # when we find the delimiter add the string after it to the list

        # 5#Hello3#you
           #i
          #j  
        res = []
        i = 0

        while i < (len(s)):
            j = i

            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length # how to know what length of string is
            res.append(s[i:j])
            i = j
        return res


            




        



