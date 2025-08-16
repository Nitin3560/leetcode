class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_total = 0
        for num in nums:
            xor_total ^= num   

        diff_bit = xor_total & -xor_total

        a = b = 0
        for num in nums:
            if num & diff_bit:
                a ^= num
            else:
                b ^= num

        return [a, b]