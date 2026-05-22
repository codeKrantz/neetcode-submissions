class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #NOT THE BEST INTERVIEW IMPLEMENTATION, JUST COOL
        return Counter(s) == Counter(t)
        