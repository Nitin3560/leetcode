class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        target = Counter(str(n))
        for i in range(31):
            power = 1 << i
            if Counter(str(power)) == target:
                return True

        return False