from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        min_ = min(nums)
        if min_ < 0:
            nums = [r + -min_ for r in nums]

        # Radix Sort
        max_ = max(nums)
        ex = 1
        while max_ // ex != 0:
            count = [0] * 10
            temp_array = [0] * len(nums)
            for item in nums:
                count[item // ex % 10] += 1
            for i in range(1, 10):
                count[i] += count[i - 1]

            for item in nums[::-1]:
                index = item // ex % 10
                temp_array[count[index] - 1] = item
                count[index] -= 1
            nums = temp_array
            ex *= 10

        max_counter = 1
        counter = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            if nums[i] == nums[i + 1] - 1:
                counter += 1
            else:
                if counter > max_counter:
                    max_counter = counter
                counter = 1

        return max(counter, max_counter)
