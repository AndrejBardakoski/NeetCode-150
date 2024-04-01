class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dictionary = {}
        for item in nums:
            if item in dictionary:
                return True
            dictionary[item] = True
        return False