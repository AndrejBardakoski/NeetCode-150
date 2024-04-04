class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        d = {}

        for s in strs:
            frequency_array = [0] * 26
            for char in s:
                frequency_array[ord(char) - ord('a')] += 1

            frequency_tuple = tuple(frequency_array)
            if frequency_tuple in d:
                d[frequency_tuple].append(s)
            else:
                d[frequency_tuple] = [s]
        list()

        return list(d.values())
