class Solution:

    def encode(self, strs: List[str]) -> str:
        #a single string
        res = ""
        for s in strs:
            #delimiter is the number of characters and then a #
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:
        #return will be a list of strings
        res = []
        i = 0
        #iterate though the string input

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            #gives the entire string
            res.append(s[j+1 : j+1+length])
            #fix i pointer
            i = j+1+length
        return res


