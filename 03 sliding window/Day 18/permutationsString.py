class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = {}
        if len(s1) > len(s2):
            return False
        for char in s1:
            d1[char] = d1.get(char, 0) + 1

        i = 0
        d2 = d1.copy()
        for j in range(len(s2)):
            char = s2[j]
            if char not in d1:
                i = j + 1
                d2 = d1.copy()
            elif char not in d2:
                while s2[i] != char:
                    d2[s2[i]] = d2.get(s2[i], 0) + 1
                    i += 1
                i += 1
            else:
                ch_count = d2[char] - 1
                if ch_count == 0:
                    d2.pop(char)
                else:
                    d2[char] = ch_count
            if len(d2) == 0:
                return True
        return False
