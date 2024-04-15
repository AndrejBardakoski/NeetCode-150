from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        iter_1 = 0
        iter_2 = len(height) - 1
        max_1 = height[iter_1]
        max_2 = height[iter_2]
        s = 0

        while iter_1 < iter_2:
            if max_1 < max_2:
                iter_1 += 1
                item = height[iter_1]
                if item > max_1:
                    max_1 = item
                else:
                    s += max_1 - item
            else:
                iter_2 -= 1
                item = height[iter_2]
                if item > max_2:
                    max_2 = item
                else:
                    s += max_2 - item

        return s
