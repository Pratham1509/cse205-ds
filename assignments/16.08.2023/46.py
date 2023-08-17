class Solution:
    def permute(self, nums):
        def solve(nums, permu, c):
            if c == len(nums):
                ans.append(list(permu))
                return
            for i in range(len(nums)):
                if permu[i] == 11:
                    permu[i] = nums[c]
                    solve(nums, permu, c + 1)
                    permu[i] = 11

        ans = []
        permu = [11] * len(nums)
        solve(nums, permu, 0)
        return ans