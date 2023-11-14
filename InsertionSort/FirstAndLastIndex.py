class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = -1
        last = -1
        for i in range(len(nums)):
            if i == target:
                first = nums[i]
            elif first != -1:
                last = nums[i]
            else:
                return first, last
