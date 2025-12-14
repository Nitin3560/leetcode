class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w = sum(1 for c in blocks[:k] if c == 'W')
        ans = w
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                w -= 1
            if blocks[i] == 'W':
                w += 1
            ans = min(ans, w)

        return ans