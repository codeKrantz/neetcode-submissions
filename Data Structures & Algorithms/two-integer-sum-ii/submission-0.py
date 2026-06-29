class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        #prioritize passing elements from the back of the list instead of the front
        while l < r:
            current = numbers[l] + numbers[r]

            if current > target:
                r -= 1
            elif current < target:
                 l += 1
            else:
                return[l+1, r+1]


        