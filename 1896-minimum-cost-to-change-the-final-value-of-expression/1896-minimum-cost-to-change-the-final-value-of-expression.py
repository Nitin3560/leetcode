class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        def merge(a, op, b):
            a0, a1 = a
            b0, b1 = b

            and0 = min(a0 + b0, a0 + b1, a1 + b0)
            and1 = a1 + b1

            or0 = a0 + b0
            or1 = min(a1 + b1, a1 + b0, a0 + b1)

            if op == '&':
                return [min(and0, or0 + 1), min(and1, or1 + 1)]
            return [min(or0, and0 + 1), min(or1, and1 + 1)]

        stack = []

        def reduce_once():
            right = stack.pop()
            op = stack.pop()
            left = stack.pop()
            stack.append(merge(left, op, right))

        def reduce_available():
            while (
                len(stack) >= 3
                and isinstance(stack[-1], list)
                and stack[-2] in '&|'
                and isinstance(stack[-3], list)
            ):
                reduce_once()

        for ch in expression:
            if ch == '0':
                stack.append([0, 1])
                reduce_available()
            elif ch == '1':
                stack.append([1, 0])
                reduce_available()
            elif ch in '&|(':
                stack.append(ch)
            else: 
                val = stack.pop()
                stack.pop() 
                stack.append(val)
                reduce_available()

        dp = stack[0]
        return dp[1] if dp[0] == 0 else dp[0]