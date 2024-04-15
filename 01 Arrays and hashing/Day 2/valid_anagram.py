class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        d = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1

        for char in t:
            if char in d and d[char] > 0:
                d[char] -= 1
            else:
                return False

        return True
