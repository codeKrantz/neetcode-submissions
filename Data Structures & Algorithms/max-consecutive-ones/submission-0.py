class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #iterate through
        maxCount = 0
        current = 0
        for num in nums:
            if num == 1:
                current += 1
            else:
                maxCount =  max(maxCount, current)
                current  = 0
        
        return max(maxCount, current)

        