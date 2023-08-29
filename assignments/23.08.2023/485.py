class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        sum=0
        maximum = []

        for i in range(len(nums)):
            if nums[i]==1:
                sum+=1
            else:
                maximum.append(sum)
                sum=0

        maximum.append(sum)
        return(max(maximum))