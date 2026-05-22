class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #O(n) time solution usings hashmap and updating until we find the correct pair
        prevMap = {} #numnber:index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        