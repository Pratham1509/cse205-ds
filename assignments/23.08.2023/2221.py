class Solution:
    def triangularSum(self, nums):
        if len(nums) == 1:
            return nums[0]
        new = []
        for i in range(len(nums)-1):
            k = (nums[i] + nums[i+1]) % 10
            new.append(k)
            
        return self.triangularSum(new)