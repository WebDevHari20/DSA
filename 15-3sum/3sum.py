class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()  # Sort to use two-pointer logic and handle duplicates easily
        
        for i in range(len(nums)):
            # If the current number is > 0, the sum can never be 0 (since the array is sorted)
            if nums[i] > 0:
                break
            
            # Skip the same element to avoid duplicate triplets in the result
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Initialize two pointers
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                
                if three_sum > 0:
                    r -= 1  # Sum too large, move right pointer left
                elif three_sum < 0:
                    l += 1  # Sum too small, move left pointer right
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    # Update pointers and skip duplicate values for l and r
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                        
        return res