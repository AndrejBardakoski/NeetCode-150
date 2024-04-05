from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for item in nums:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1

        sorted_freq = sorted(freq.items(), key=lambda fr: fr[1], reverse=True)[:k]
        return [x[0] for x in sorted_freq]
