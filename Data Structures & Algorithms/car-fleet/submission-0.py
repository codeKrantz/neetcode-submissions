class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #zip function combines the two lists together so the car is with its speed -> allows us to sort the cars 
        pair = [[p,s] for p, s in zip(position, speed)]
        
        #stores the number of car fleets
        stack = []
        for p,s in sorted(pair)[::-1]:
            #reverse sorted order
            stack.append((target - p) / s)
            #does it overlap with previouse fleets
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                #collision
                stack.pop()

        return len(stack)



        