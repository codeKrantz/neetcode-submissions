class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        current_max = 0
        while l <= r:
            length = r - l
            shortest = min(heights[l], heights[r])

            if (shortest*length) > current_max:
                current_max = shortest*length
            
            if shortest == heights[l]:
                l += 1
            else:
                r -= 1
        return current_max


        