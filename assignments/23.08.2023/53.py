class Solution:
    def maxSubArray(self, nums):
        sum = 0
        max_sum = nums[0]
        for i in range(len(nums)):
            sum += nums[i]
            if sum > max_sum:
                max_sum = sum
            if sum < 0:
                sum = 0
        return max_sum