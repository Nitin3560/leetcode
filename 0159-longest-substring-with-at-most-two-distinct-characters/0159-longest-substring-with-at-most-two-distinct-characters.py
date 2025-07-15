class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        left = 0
        max_len = 0
        char_map = defaultdict(int)

        for right in range(len(s)):
            char_map[s[right]] += 1
            while len(char_map) > 2:
                char_map[s[left]] -= 1
                if char_map[s[left]] == 0:
                    del char_map[s[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
