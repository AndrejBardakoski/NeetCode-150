class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 1
        char_i = s[i]
        d = {}
        max_len = 0
        num_replacements = 0
        for j in range(1, len(s)):
            char_j = s[j]
            d[char_j] = d.get(char_j, 0) + 1
            if char_i != char_j:
                num_replacements += 1
                while num_replacements > k:
                    if i == j:
                        num_replacements = 0
                        char_i, i = char_j, j
                        continue
                    i += 1
                    char_i, = s[i]
                    d[char_i] -= 1
                    num_replacements = j - i - d[char_i]

            max_len = max(max_len, j - i + 1)

        max_len = max(max_len, j - i + 1 + min(k - num_replacements, i))
        while i < j:
            i += 1
            char_i, = s[i]
            d[char_i] -= 1
            num_replacements = j - i - d[char_i]
            max_len = max(max_len, j - i + 1 + min(k - num_replacements, i))
        return max_len


# TO DO
# Remove l add everything in d

if __name__ == '__main__':
    s = Solution()
    x = s.characterReplacement("ABCDDD", 3)
    print(x)
