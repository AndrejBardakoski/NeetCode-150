from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_product = [nums[0]]
        for i in range(1, len(nums)):
            right_product.append(right_product[i - 1] * nums[i])

        left_product = [nums[-1]]
        for i in range(1, len(nums)):
            left_product.append(left_product[i - 1] * nums[-i - 1])

        left_product.reverse()

        output = [left_product[1]]
        for i in range(1, len(nums) - 1):
            output.append(left_product[i + 1] * right_product[i - 1])
        output.append(right_product[len(nums) - 2])
        return output
