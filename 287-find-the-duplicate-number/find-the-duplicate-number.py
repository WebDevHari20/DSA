class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)-1
        nums.sort()
        for i in range (n):
            if nums[i]==nums[i+1]:
                return nums[i]
                break;