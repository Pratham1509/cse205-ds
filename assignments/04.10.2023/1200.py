class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
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
        arr=sort(arr)
        min_diff=min(arr[i+1]-arr[i] for i in range(len(arr)-1))
        ans=[]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==min_diff:
                ans.append([arr[i],arr[i+1]])
        return ans
