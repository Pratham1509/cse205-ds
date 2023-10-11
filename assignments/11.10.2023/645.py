class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        newnums=[]
        n=len(nums)
        for i in nums:
            if nums.count(i)==2:
                newnums.append(i)
                nums.remove(i)
                break
        for i in range(1,n+1):
            if i not in nums:
                newnums.append(i)
                break
        return newnums