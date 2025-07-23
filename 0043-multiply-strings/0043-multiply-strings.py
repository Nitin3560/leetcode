class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        res = [0] * (len(num1) + len(num2))
        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                total = mul + res[p2]

                res[p1] += total // 10
                res[p2] = total % 10

        result = []
        for digit in res:
            if not (len(result) == 0 and digit == 0):
                result.append(str(digit))

        return ''.join(result) if result else "0"
        