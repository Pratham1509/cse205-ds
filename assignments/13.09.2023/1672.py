class Solution(object):
    def maximumWealth(self, accounts):
        ans=0
        for i in range(len(accounts)):
            curr_sum=sum(accounts[i])
            ans=max(ans,curr_sum)
        return ans
        