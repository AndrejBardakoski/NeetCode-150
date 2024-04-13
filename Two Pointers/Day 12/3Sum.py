from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        neg_nums = []
        pos_nums = []
        zero = 0

        for item in nums:
            if item < 0:
                neg_nums.append(item)
            elif item == 0:
                zero += 1
            else:
                pos_nums.append(item)

        result = []

        for iter1 in range(len(neg_nums)):
            if iter1 > 0 and neg_nums[iter1] == neg_nums[iter1 - 1]:
                continue
            item = neg_nums[iter1]
            iter2 = 0
            iter3 = len(pos_nums) - 1
            while iter2 < iter3:
                s = pos_nums[iter2] + pos_nums[iter3] + item
                if s < 0:
                    iter2 += 1
                elif s > 0:
                    iter3 -= 1
                else:
                    result.append([item, pos_nums[iter2], pos_nums[iter3]])
                    iter2 += 1
                    while iter2 < iter3 and pos_nums[iter2] == pos_nums[iter2 - 1]:
                        iter2 += 1
                    iter3 -= 1
                    while iter2 < iter3 and pos_nums[iter3] == pos_nums[iter3 + 1]:
                        iter3 -= 1

            if zero > 0 and -neg_nums[iter1] in pos_nums:
                result.append((item, 0, -item))

        for iter1 in range(len(pos_nums)):
            if iter1 > 0 and pos_nums[iter1] == pos_nums[iter1 - 1]:
                continue
            item = pos_nums[iter1]
            iter2 = 0
            iter3 = len(neg_nums) - 1
            while iter2 < iter3:
                s = neg_nums[iter2] + neg_nums[iter3] + item
                if s < 0:
                    iter2 += 1
                elif s > 0:
                    iter3 -= 1
                else:
                    result.append([neg_nums[iter3], neg_nums[iter2], item])
                    iter2 += 1
                    while iter2 < iter3 and neg_nums[iter2] == neg_nums[iter2 - 1]:
                        iter2 += 1
                    iter3 -= 1
                    while iter2 < iter3 and neg_nums[iter3] == neg_nums[iter3 + 1]:
                        iter3 -= 1

        if zero >= 3:
            result.append([0, 0, 0])

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([0, 0, 0]))
