class Solution(object):
    def subsetsWithDup(self, nums):
        
        res=[]
        def getSubset(index,subset):
           
            if index==len(nums):
                res.append(subset[::])
                return
            
            subset.append(nums[index])    
            
            getSubset(index+1,subset)
            
            subset.pop()
            
            while index<len(nums)-1 and nums[index]==nums[index+1]:
                index+=1
            getSubset(index+1,subset)    
        
        nums.sort()
        getSubset(0,[])  
        return res