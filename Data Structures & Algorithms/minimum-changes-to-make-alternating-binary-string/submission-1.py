class Solution:
    def minOperations(self, s: str) -> int:
        #only 2 patterns: starts with 0 or 1
        mismatches = 0

        #getting index AND the value
        for i, char in enumerate(s):
            #enables checking by index by assuming that index 0 should be a 0
            expected = '0' if i % 2 == 0 else '1'

            if char != expected:
                mismatches += 1
        #min is used in case the pattern is starting with 1
        return min(mismatches, len(s) - mismatches)
        