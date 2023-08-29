class Solution(object):
    def findKthPositive(self, arr, k):
        arr1=[]
        for i in range(0,len(arr)+k+1):
            if i not in arr:
                arr1.append(i)
        return arr1[k]                