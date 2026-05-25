class Solution:
    def isPalindrome(self, s: str) -> bool:
        #lots of built in functions, but a valid solution
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        return newStr == newStr[::-1]
