class Solution(object):
    def diffWaysToCompute(self, expression):
        memo = {}

        def ways(expr):
            if expr in memo:
                return memo[expr]
            
            results = []
            for i, char in enumerate(expr):
                if char in '+-*':
                    left_results = ways(expr[:i])
                    right_results = ways(expr[i+1:])

                    for l in left_results:
                        for r in right_results:
                            if char == '+':
                                results.append(l + r)
                            elif char == '-':
                                results.append(l - r)
                            elif char == '*':
                                results.append(l * r)

            if not results:
                results.append(int(expr))

            memo[expr] = results
            return results

        return ways(expression)
