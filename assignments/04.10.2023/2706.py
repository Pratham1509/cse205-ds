class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
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
        prices=sort(prices)
        for i in range(len(prices)-1):
            choco_price=prices[i]+prices[i+1]
            if choco_price<=money:
                money=money-choco_price
                return money
        return money
