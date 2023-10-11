class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left, right = arr[:mid], arr[mid:]
            left, right = sort(left), sort(right)
            ans, i, j = [], 0, 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    ans.append(left[i])
                    i += 1
                else:
                    ans.append(right[j])
                    j += 1
            ans.extend(left[i:])
            ans.extend(right[j:])
            return ans
        ans=sort(nums)
        if ans[0]!=0:
            return 0
        if len(ans)==1 and ans[0]!=0:
            return 0
        for i in range(len(ans)-1,-1,-1):
            if ans[i]-ans[i-1]!=1:
                return ans[i-1]+1
