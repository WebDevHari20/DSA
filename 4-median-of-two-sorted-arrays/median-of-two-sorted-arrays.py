from math import *
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        combined = sorted(nums1+nums2)
        n = len(combined)
        if n%2 != 0:
            return float(combined[n//2])
        else:
            a = n//2
            b = a-1
            return (combined[a]+combined[b])/2.0
        