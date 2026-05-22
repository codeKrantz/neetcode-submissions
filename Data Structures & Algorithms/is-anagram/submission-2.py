class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #O(1) memeory implemntation, worse time
        return sorted(s) == sorted(t)