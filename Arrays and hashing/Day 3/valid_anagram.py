class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            item = nums[i]
            if item in d:
                return [d[item], i]
            else:
                d[target - item] = i
