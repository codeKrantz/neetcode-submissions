class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #explicit implementation

        #check length for fast fail
        if len(s) != len(t):
            return False
        
        #Use hashmap to quickly count then only interate once though the words
        mapS, mapT = {},{}

        for letter in range(len(s)):
            #get returns 0 if not found yet
            mapS[s[letter]] = 1 + mapS.get(s[letter], 0)
            mapT[t[letter]] = 1 + mapT.get(t[letter], 0)

        #Now checking letters
        for c in mapS:
            if mapS[c] != mapT.get(c, 0):
                return False
        
        return True
        