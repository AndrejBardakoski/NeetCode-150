class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        i = 0
        max_len = 0
        for j in range(len(s)):
            ch = s[j]
            if ch in d and d[ch] >= i:
                i = d[ch] + 1
            d[ch] = j
            max_len = max(max_len, j - i + 1)
        return max_len
