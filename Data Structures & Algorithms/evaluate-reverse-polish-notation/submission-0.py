class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                #keep the answer in the stack for future operations
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                right =  stack.pop()
                left = stack.pop()
                stack.append(left-right)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                right =  stack.pop()
                left = stack.pop()
                #rounds towards zero
                stack.append(int(left/right))
            else:
                stack.append(int(c))
        return stack[0]
        