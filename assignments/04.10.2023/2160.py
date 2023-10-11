class Solution:
    def minimumSum(self, num: int) -> int:
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
        s=sort(str(num))
        s1=int(s[0]+s[2])
        s2=int(s[1]+s[3])
        return s1+s2
        
        
        