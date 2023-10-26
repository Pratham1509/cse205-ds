class Solution:
    def largestInteger(self, num: int) -> int:
        p = [] 
        q = [] 
        nums = str(num) 
        n = len(nums) 
        for i in range(n):
            digit = int(nums[i])
            if digit % 2:
                heapq.heappush(p, -digit)
            else:
                heapq.heappush(q, -digit) 
        answer = 0
        for i in range(n):
            answer *= 10
            if int(nums[i]) % 2: 
                answer += -heapq.heappop(p)
            else:
                answer += -heapq.heappop(q) 
        return answer
        