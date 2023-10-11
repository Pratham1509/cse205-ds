class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
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
        dict_ar1 = collections.Counter(arr1)
        new_arr = []
        for num in arr2:
            if num in dict_ar1:
                [new_arr.append(num) for _ in range(dict_ar1[num])]

        for num in new_arr:
            arr1.remove(num)
        arr1=sort(arr1)
        return new_arr + arr1