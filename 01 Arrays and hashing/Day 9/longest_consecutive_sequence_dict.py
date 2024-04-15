from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        result = 0

        for num in nums:
            if num not in d:
                low = num if num - 1 not in d else d[num - 1][0]
                high = num if num + 1 not in d else d[num + 1][1]
                d[num] = [low, high]
                d[low][1] = high
                d[high][0] = low
                result = max(result, high - low + 1)
        return result
