class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
            
        arr = code + code
        res = [0] * n
        m = abs(k)

        if k > 0:
            left, right = 1, k
        else:
            left, right = n - m, n - 1
        window_sum = sum(arr[left:right + 1])
        for i in range(n):
            res[i] = window_sum
            window_sum -= arr[left]
            left += 1
            right += 1
            window_sum += arr[right]

        return res