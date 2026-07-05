class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # Try deleting either the left or right character,
                # and check if the ENTIRE remaining substring is a palindrome.
                return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)

        return True