class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            min = i
            for j in range(i+1,n):
                if nums[min] > nums[j]:
                    min = j
            
            nums[i], nums[min] = nums[min], nums[i]      
        
