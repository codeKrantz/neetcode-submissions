class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        #left pointer
        l = 0
        result = 0

        #right pointer
        for r in range(len(s)):
            #sets will only have one value -> fast duplicate check
            while s[r] in charSet:
                #update window
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result = max(result, r-l+1)
        return result