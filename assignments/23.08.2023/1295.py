class Solution(object):
    def findNumbers(self, nums):
        def digits(num):
            count=0
            while num!=0:
                num//=10
                count+=1 
            return count
        sum=0
        for i in nums:
            if digits(i)%2==0:
                sum+=1
        return sum