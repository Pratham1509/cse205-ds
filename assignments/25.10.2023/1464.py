class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]] = i
        sorted_nums = sorted(nums, reverse=True)
        i = mp[sorted_nums[0]]
        j = mp[sorted_nums[1]]
        return (nums[i]-1) * (nums[j]-1)
        