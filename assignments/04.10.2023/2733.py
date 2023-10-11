class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return -1
        for i in nums:
            if i!=max(nums) and i!=min(nums):
                return i
                