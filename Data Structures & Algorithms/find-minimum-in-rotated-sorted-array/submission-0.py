class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Brute Force
        minElement = nums[0]
        for num in nums:
            minElement = min(minElement, num)
        
        return minElement
        